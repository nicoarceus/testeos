select table_name,column_name, udt_name,character_maximum_length
from information_schema.columns
where table_name = 'usuarios';