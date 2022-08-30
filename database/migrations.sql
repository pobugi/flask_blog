CREATE TABLE IF NOT EXISTS public.file
(
    id serial NOT NULL,
    title character varying NOT NULL,
    extension character varying,
    owner_id integer NOT NULL,
    path character varying,
    created timestamp with time zone,
    updated timestamp with time zone,
    CONSTRAINT file_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.user
(
    id serial NOT NULL,
    username character varying NOT NULL,
    created timestamp with time zone,
    updated timestamp with time zone,
    CONSTRAINT user_pkey PRIMARY KEY (id),
    CONSTRAINT user_username_unique UNIQUE (username)
);


CREATE TABLE IF NOT EXISTS public.post
(
    id serial NOT NULL,
    title character varying NOT NULL,
    description character varying NOT NULL,
    owner_id integer NOT NULL,
    created timestamp with time zone,
    updated timestamp with time zone,
    CONSTRAINT post_pkey PRIMARY KEY (id)
);
