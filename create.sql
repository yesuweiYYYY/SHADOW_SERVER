create Table Users(ID int,X int,Y int, Z int)


create Table Users(
    username char(20) not null,
     password char(20) not null,
      sex  char (20) ,
       age char(20) ,
    phone char(20) ,
     descrption char(40) ,
    image char(254)
               );


-- create Table location(
--     usrname char(20) not null primary key,
--     orient int,
--     distance int
--                );

create Table location(
    id char(20) not null primary key,
    x float,
    y float
               );

create Table relation(
    username char(20) not null primary  key,
    id char(20) not null
)
