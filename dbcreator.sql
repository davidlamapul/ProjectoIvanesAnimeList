CREATE DATABASE IF NOT EXISTS ANIMELIST;
USE ANIMELIST;

CREATE TABLE USUARIO (
IdUser int,
Username varchar(32) unique,
EMail varchar(64) unique not null,
Pass varchar(64) not null
);

CREATE TABLE ANIME (
IdAnime int,
Nombre varchar(64) unique not null,
Estreno int,
EpTotal int not null
);

CREATE TABLE IF NOT EXISTS USUARIO_ANIME (
RIdUser int not null,
RIdAnime int not null,
EpVistos int null default 0,
Estado varchar(30)
);

ALTER TABLE USUARIO
ADD CONSTRAINT PK_USUARIO PRIMARY KEY (IdUser),
MODIFY IdUser int auto_increment;

ALTER TABLE ANIME
ADD CONSTRAINT PK_ANIME PRIMARY KEY (IdAnime),
MODIFY IdAnime int auto_increment;

ALTER TABLE USUARIO_ANIME
ADD CONSTRAINT FK_USUARIO_ANIME_ANIME FOREIGN KEY (RIdAnime) REFERENCES ANIME(IdAnime),
ADD CONSTRAINT FK_USUARIO_ANIME_USUARIO FOREIGN KEY (RIdUser) REFERENCES USUARIO(IdUser);