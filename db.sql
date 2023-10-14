CREATE TABLE IF NOT EXISTS `nekogram_users` (
  `id` bigint(20) NOT NULL PRIMARY KEY ,
  `username` varchar(100) DEFAULT NULL,
  `full_name` varchar(100) NOT NULL,
  `last_message_id` int(11) DEFAULT NULL,
  `data` longtext NOT NULL DEFAULT '{}',
  `lang` varchar(2) NOT NULL
);
--
CREATE TABLE IF NOT EXISTS `search_cache` (
    `url` varchar(500) NOT NULL PRIMARY KEY
);