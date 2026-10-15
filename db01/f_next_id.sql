drop function f_next_id;
create function f_next_id(p_table text) returns integer as $$
declare
  c int;
begin
  execute format('select max(id) from  %I', p_table) into c;
  return c;
end;
$$ language plpgsql;
