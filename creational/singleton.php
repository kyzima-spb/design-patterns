<?php

/**
 * Singleton
 *
 * Гарантирует, что у класса есть только один экземпляр,
 * и предоставляет к нему глобальную точку доступа.
 */


class Singleton
{
    static private $instance;

    private function __construct() {}

    private function __clone() {}

    static public function getInstance()
    {
        if (!static::$instance) {
            static::$instance = new static();
        }
        return static::$instance;
    }
}


class Config extends Singleton
{
    private $params = [];

    public function get(string $name)
    {
        return isset($this->params[$name]) ? $this->params[$name] : null;
    }

    public function set(string $name, $value)
    {
        $this->params[$name] = $value;
    }
}


$config1 = Config::getInstance();
$config2 = Config::getInstance();
var_dump($config1 === $config2);

$config1->set('db_host', 'localhost');
var_dump($config2->get('db_host'));
