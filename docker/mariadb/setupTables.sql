drop table if exists Task;
drop table if exists Task_Recurrence;
drop table if exists Individual;
drop table if exists Housemate;
drop table if exists User_Relation;
drop table if exists Task_State;
drop table if exists House;
drop table if exists House_Status;

-- drop table if exists Login;
-- drop table if exists Users;

-- create table Users
-- (
-- 	username INT(10) comment 'A Unique Username',
-- 	name NVARCHAR(64) not null comment 'Real Name of User',
-- 	cr_date DATETIME default NOW() not null comment 'Account Creation Date.'
-- )
-- comment 'Stores a users username, name and account creation date.';

-- create unique index Users_username_uindex
-- 	on Users (username); -- A username MUST be unique!

-- alter table Users
-- 	add constraint Users_pk
-- 		primary key (username); -- Username is the primary key for the users table.


create table House_Status
(
	status_id int auto_increment COMMENT 'The ID of the combination of Level and Wear',
	level_num int not null COMMENT 'The level number',
	level_name VARCHAR(16) not null COMMENT 'The name of the level i.e Penthouse or Hut',
	wear_level VARCHAR(16) not null COMMENT 'Either degraded or pristine',
    constraint House_Status_pk
		primary key (status_id)
);

create unique index House_Status_status_id_uindex
	on House_Status (status_id);


create table House
(
	house_id int auto_increment COMMENT 'The ID of the house',
	status_id int default 0 not null COMMENT 'The house current status',
	maintain_req int default 0 not null COMMENT 'The number of weekly tasks required',
	constraint House_HouseStatus__fk
		foreign key (status_id) references House_Status (status_id),
		constraint House_pk
		primary key (house_id)
);

create unique index House_house_id_uindex
	on House (house_id);


create table User_Relation
(
	relation_id int auto_increment COMMENT 'The ID of a singular relationship',
	user_id INT(10) COMMENT 'The username for the relationship',
	constraint User_Relation_auth_user_id_fk
		foreign key (user_id) references djangoData.auth_user (id),
		constraint User_Relation_pk
		primary key (relation_id)
);

create unique index User_Relation_relation_id_uindex
	on User_Relation (relation_id);


create table Housemate
(
	relation_id int not null COMMENT 'The ID of a singular relationship',
	user_id INT(10) COMMENT 'The username for the relationship',
	house_id int not null COMMENT 'The house ID for the relationship',
	constraint Housemate_House_house_id_fk
		foreign key (house_id) references House (house_id)
			on delete cascade,
	constraint Housemate_User_Relation_relation_id_fk
		foreign key (relation_id) references User_Relation (relation_id)
			on delete cascade,
	constraint Housemate_auth_user_id_fk
		foreign key (user_id) references djangoData.auth_user (id)
			on delete cascade
);

create unique index Housemate_relation_id_uindex
	on Housemate (relation_id);


create table Individual
(
	relation_id int not null COMMENT 'The ID of a singular relationship',
	user_id INT(10) COMMENT 'The username for the relationship',
	constraint Individual_User_Relation_relation_id_fk
		foreign key (relation_id) references User_Relation (relation_id)
			on delete cascade,
	constraint Individual_auth_user_id_fk
		foreign key (user_id) references djangoData.auth_user (id)
			on delete cascade
);


create table Task_State
(
	task_state_id int auto_increment COMMENT 'The numerical ID of a particular task state',
	state_name NVARCHAR(16) not null COMMENT 'The text string of the task state i.e finished, cancelled, etc',
	constraint Task_State_pk
		primary key (task_state_id)
);

create unique index Task_State_state_name_uindex
	on Task_State (state_name);

create unique index Task_State_task_state_id_uindex
	on Task_State (task_state_id);


create table Task_Recurrence
(
	recur_id int auto_increment COMMENT 'The ID for a single recurrence entry',
	freq_time TIME default SEC_TO_TIME(0) not null COMMENT 'Every X hours and X minutes the task will repeat',
	freq_days TINYINT default 0 not null COMMENT 'Every X days the task will repeat',
	freq_weeks TINYINT default 0 not null COMMENT 'Every X weeks the task will repeat',
	freq_year BOOL default FALSE not null COMMENT 'Every 1 year the task will repeat',
	constraint Task_Recurrence_pk
		primary key (recur_id)
);

create unique index Task_Recurrence_recur_id_uindex
	on Task_Recurrence (recur_id);


create table Task
(
	task_id int auto_increment comment 'The ID for a ',
	relation_id int not null,
	task_elo int default 0 not null comment 'read: task score',
	assign_date DATE default CURDATE() null,
	deadline_date DATETIME null,
	has_recur BOOL default FALSE not null,
	recur_id int null,
	state_id int not null,
	constraint Task_Task_Recurrence_recur_id_fk
		foreign key (recur_id) references Task_Recurrence (recur_id)
			on delete cascade,
	constraint Task_Task_State_task_state_id_fk
		foreign key (state_id) references Task_State (task_state_id)
			on delete cascade,
	constraint Task_User_Relation_relation_id_fk
		foreign key (relation_id) references User_Relation (relation_id)
			on delete cascade,
			constraint Task_pk
		primary key (task_id)
);

create unique index Task_recur_id_uindex
	on Task (recur_id);

create unique index Task_task_id_uindex
	on Task (task_id);