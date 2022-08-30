import os

from flask import Blueprint, jsonify, request
from flask import current_app, g

from src.api.file.models import File
from src.auth.views import auth

file_api = Blueprint("file_api", __name__)


@file_api.route("/", methods=["GET"])
def create_user():
    return jsonify({"hello": "world"})


@file_api.route("/file", methods=["POST"])
def upload_file():
    import hashlib
    from src.api.file.utils import FileUtils

    submitted_file = request.files.get("file")
    if not submitted_file:
        return jsonify({"success": False, "error": "File was not attached"}), 400

    img_key = hashlib.md5(submitted_file.read()).hexdigest()
    from src.utils.string_utils import StringUtils

    filename = submitted_file.filename
    # filename = secure_filename(submitted_file.filename)
    filename = StringUtils.to_latin(filename)
    # file_path_root = current_app.config["ROOT_FILE_FOLDER"]
    # file_path = os.path.join(file_path_root, img_key[:2])
    file_type = submitted_file.content_type

    file_path = FileUtils.create_folder(img_key[:2])

    if os.path.isfile(os.path.join(file_path, filename)) is False:
        file = File.create(
            title=filename,
            extension=file_type,
            owner_id=324,
            path=current_app.config["ROOT_FILE_FOLDER"],
        )
        submitted_file.save(os.path.join(file_path, filename))

        import hashlib

        BUF_SIZE = 65536
        BUF_SIZE = 1000

        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        with open(os.path.join(file_path, filename), "rb") as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                md5.update(data)
                sha1.update(data)

        return jsonify(
            {
                "success": True,
                "file": File.to_dict(file),
                "md5": md5.hexdigest(),
                "sha1": sha1.hexdigest(),
                "img_key": img_key,
            }
        )
    else:
        return jsonify({"success": False, "error": "File already exists", "fileExist": True})


# @user_api.route("/registration", methods=["POST"])
# def register_user_email():
#     data_dict = request.json
#     email = data_dict.get("email").strip()
#
#     if not EmailValidator.validate(email):
#         return raise_with_error("Wrong email format")
#
#     if UserEmail.get(email):
#         return raise_with_error("Указанный email уже зарегистрирован в системе")
#     user_email = UserEmail.create(email=email)
#     if not user_email.email:
#         return raise_with_error("email was not provided")
#     return jsonify(UserEmail.to_dict(user_email))
#     # from IAPI.api.unaprofile.utils import UnaProfileUtils
#     #
#     # email_sent_status = UnaProfileUtils.generate_token_and_send_email(profile_email.email)
#     # if email_sent_status == 202:
#     #     profile_email = ProfileEmail.register_sent_confirmation_message(profile_email.email)
#     # return jsonify(ProfileEmail.to_dict(profile_email))
#
#
@file_api.route("/file", methods=["GET"])
@auth.login_required
def get_all_files():
    files = File.get_all()
    return jsonify(File.to_dict_multi(files))


@file_api.route("/smoke", methods=["GET"])
@auth.login_required
def smk():
    return jsonify({"123": 456})
