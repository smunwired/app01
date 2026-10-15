drop procedure reset_sequences;
create procedure reset_sequences()
language plpgsql as
$$
declare
  command RECORD;
  command_cursor CURSOR FOR
        SELECT
            'SELECT SETVAL(' ||
               quote_literal(quote_ident(sequence_namespace.nspname) || '.' || quote_ident(class_sequence.relname)) ||
               ', COALESCE(MAX(' ||quote_ident(pg_attribute.attname)|| '), 1) ) FROM ' ||
               quote_ident(table_namespace.nspname)|| '.'||quote_ident(class_table.relname)|| ';' AS command
        FROM pg_depend
            INNER JOIN pg_class AS class_sequence
                ON class_sequence.oid = pg_depend.objid
                    AND class_sequence.relkind = 'S'
            INNER JOIN pg_class AS class_table
                ON class_table.oid = pg_depend.refobjid
            INNER JOIN pg_attribute
                ON pg_attribute.attrelid = class_table.oid
                    AND pg_depend.refobjsubid = pg_attribute.attnum
            INNER join pg_type
                ON pg_type.oid = pg_attribute.atttypid
            INNER JOIN pg_namespace as table_namespace
                ON table_namespace.oid = class_table.relnamespace
            INNER JOIN pg_namespace AS sequence_namespace
                ON sequence_namespace.oid = class_sequence.relnamespace
        WHERE pg_type.typname ilike '%int%' and class_sequence.relname != 'rtv_quantity_id_seq'
        ORDER BY sequence_namespace.nspname, class_sequence.relname;
BEGIN
  FOR command IN command_cursor LOOP
     raise info 'Command %' , command.command;
     execute command.command;
  END LOOP;
end ;
$$;
