<div align=center>
    <font size = 18>
DRL in solving smart port
    </font>
</div>
[![Stargazers repo roster for @LeeXzhou/DRL-for-Smart-Port](https://reporoster.com/stars/LeeXzhou/DRL-for-Smart-Port)](https://github.com/LeeXzhou/DRL-for-Smart-Port/stargazers)

[![Forkers repo roster for @LeeXzhou/DRL-for-Smart-Port](https://reporoster.com/forks/LeeXzhou/DRL-for-Smart-Port)](https://github.com/LeeXzhou/DRL-for-Smart-Port/network/members)

# File structure

```
DRL4SmartPort

.
├── envrionment        # to_delete?  deprecated.  
│   ├── berth.py
│   ├── boat_move.py
│   ├── goods_generate.py
│   ├── port_environment.py
│   ├── robot_move.py
│   └── utils.py
├── maps
├── src
│   ├── agent
│   ├── consts.py       # save global consts
│   ├── env
│   │   └── smart_port.py
│   └── utils
│       ├── logger.py   
│       ├── map_util.py
│       └── misc.py     # other util functions that are not easy to classify
└── test
    └── test.py         # pytest file
```

### environment

- port_environment.py: 
- robot_move.py: 
- utils.py: record a global variable "Map", and supply some useful functions



# Others

## Angular Commit Message Convention
```
<type>(<scope>): <short summary>
  │       │             │
  │       │             └─⫸ Summary in present tense. Not capitalized. No period at the end.
  │       │
  │       └─⫸ Commit Scope: animations|bazel|benchpress|common|compiler|compiler-cli|core|
  │                          elements|forms|http|language-service|localize|platform-browser|
  │                          platform-browser-dynamic|platform-server|router|service-worker|
  │                          upgrade|zone.js|packaging|changelog|docs-infra|migrations|ngcc|ve|
  │                          devtools....
  │
  └─⫸ Commit Type: build|ci|doc|docs|feat|fix|perf|refactor|test
                    website|chore|style|type|revert
```
