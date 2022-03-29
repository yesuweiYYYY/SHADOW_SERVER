



create Table Users
(
    username char(20) not null,
     password char(20) not null,
      sex  char (20) ,
       age char(20) ,
    phone char(20) ,
     descrption char(40) ,
    image char(254)
);


-- test
create Table location
(
    id char(20) not null primary key,
    x float,
    y float
);


create Table relation
(
    username char(20) not null primary  key,
    id char(20) not null
)

-- 初始化数据
insert into Users values("ysw","ysw123","男","18","123456","123456","123456");
insert into Users values("nzz","nzz123","男","18","123456","123456","123456");
insert into Users values("gwd","gwd123","男","18","123456","123456","123456");


insert into relation values("ysw","YSW");
insert into relation values("nzz","NZZ");
insert into relation values("gwd","GWD");

insert into location values("YSW",1,5);
insert into location values("NZZ",2,3);
insert into location values("GWD",6,2);