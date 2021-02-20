# плейбук Ansible
## Задачи:
- ставит nginx, zsh, wget
- клонирует из git в /var/www/ очень простую web страничку "Under construction"
- кладет новую конфигурацию nginx которая направляет на эту страничку
- настраивает в sysctl параметр fs.files-max в 1204000 и somaxconn в 65535
- прописывает на этой машинке 2 разных ssh ключа в /root
Целевая ОС - ubuntu 18.04LTS

В проекте использовались две виртуальные машины  Ubuntu 18.04 на VirtualBox.
## Структура проекта:
```
.
├── ansible-test
│   ├── ansible.cfg
│   ├── group_vars
│   │   └── test
│   ├── hosts
│   ├── play.yml
│   ├── README.md
│   ├── roles
│   │   ├── epel
│   │   │   └── tasks
│   │   │       └── main.yml
│   │   ├── git
│   │   │   └── tasks
│   │   │       └── main.yml
│   │   ├── nginx
│   │   │   ├── handlers
│   │   │   │   └── main.yml
│   │   │   ├── tasks
│   │   │   │   └── main.yml
│   │   │   ├── templates
│   │   │   │   ├── default.j2
│   │   │   │   ├── index.html.j2
│   │   │   │   ├── nginx.conf
│   │   │   │   └── nginx_vhosts.conf
│   │   │   └── vars
│   │   │       └── main.yml
│   │   ├── sshkey
│   │   │   └── tasks
│   │   │       └── main.yml
│   │   ├── sysctl
│   │   │   └── tasks
│   │   │       ├── main.yml
│   │   │       ├── scripts
│   │   │       │   ├── somaxconn_change.sh
│   │   │       │   └── sysctl_change.sh
│   │   │       └── vars
│   │   │           └── sysctlparam.yml
│   │   └── utils
│   │       └── tasks
│   │           └── main.yml
│   └── tree.txt
├── inventory
├── playbooks
│   └── site.yml
└── roles
    └── nginx
        └── tasks
            └── main.yml

```

* [Вывод парометров на целевой машине до и после запуска плейбука](test.txt)

# ToDo:
- теги
- переменные
- комментарии

- рассмотреть варианты и с временной заменой параметров, и с простоянной.
- рассмотреть необходимость принудительного выполнения некоторых задач.
