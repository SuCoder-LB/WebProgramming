create table flights(
    id integer primary key autoincrement ,
    origin text not null ,
    destination text not null ,
    duration integer not null
);
select * from flights;

insert into flights(origin, destination, duration) values ("new york","london",415);
select * from flights;

insert into flights(origin, destination, duration) values ("","london",415);
insert into flights(origin, destination, duration) values ("shanghai","paris",760);
insert into flights(origin, destination, duration) values ("istanbul","tokyo",700);
insert into flights(origin, destination, duration) values ("new york","paris",435);
insert into flights(origin, destination, duration) values ("moscow","paris",245);
insert into flights(origin, destination, duration) values ("lima","new york",455);



select * from flights;

.mode column
.header on

select * from flights;

select *
from flights;

select * from flights where origin = "new york";

select *from flights where duration>700;
select *from flights where duration>500 or destination="paris";
select *from flights where origin in ("shanghai","istanbul");

select *from flights where origin like "%a%";

update flights set duration=430 where origin = "new york" and destination ="london";

delete from flights where id=2;