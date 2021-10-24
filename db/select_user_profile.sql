select * from users;

select * from addresses;

select * from phones;

select * from users
join addresses on addresses.user_id = users.id;

select * from users
join phones on phones.user_id = users.id;