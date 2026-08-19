delimiter //
drop trigger if exists tr_crdn_i//
create trigger tr_crdn_i 
before insert on crdn 
for each row 
  begin 
    declare v_last_id int;
    if new.crdd is null then
      select last_insert_id() into v_last_id;
      set new.crdd = v_last_id+1, new.dtm = '1000-01-01';
    else
      if new.dtm is null then
        set new.dtm = now();
      end if;
    end if;
  end;
//
delimiter ;
