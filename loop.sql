SELECT * FROM Personage;
CREATE TABLE Personagecopy AS SELECT * FROM Personage;
SELECT * FROM Personagecopy;


DO $$
DECLARE
	pers_name		Personagecopy.pers_name%TYPE;
	pers_weapon		Personagecopy.pers_weapon%TYPE;
	pers_feature	Personagecopy.pers_feature%TYPE;
	pers_main_role	Personagecopy.pers_main_role%TYPE;


BEGIN
	pers_name := 'Venti';
	pers_weapon := 'Bow';
	pers_feature := 'Anemo';
	pers_main_role := 'Support';
	
	FOR counter in 1..5
		LOOP
			INSERT INTO Personagecopy(pers_name, pers_weapon, pers_feature, pers_main_role)
				VALUES (pers_name || counter, pers_weapon, pers_feature, pers_main_role);
		END LOOP;
END;
$$