delimiter $$
create function f_title(p_id int) returns varchar(100)
begin 
	declare v_str varchar(100); 
	select title into v_str 
	from title 
	where id=p_id; 
	
	return v_str; 
end
$$
delimiter ;
