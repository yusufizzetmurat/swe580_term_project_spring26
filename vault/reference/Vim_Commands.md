---
tags: [reference, tools, linux]
created: 2026-01-30T09:00:00
modified: 2026-01-30T09:00:00
---

# Vim Commands

Quick reference for Vim. I use Vim mostly for editing config files and quick edits on remote servers via [[SSH_Guide]]. For serious coding, VSCode with SSH remote extension is better.

## Modes

- **Normal mode**: default, for navigation and commands. Press `Esc` to return here from anywhere.
- **Insert mode**: `i` (before cursor), `a` (after cursor), `o` (new line below), `O` (new line above)
- **Visual mode**: `v` (character), `V` (line), `Ctrl+V` (block)
- **Command mode**: `:` for ex commands

## Essential Navigation

```
h j k l         left, down, up, right
w / b           next / previous word
0 / $           start / end of line
gg / G          start / end of file
Ctrl+D / Ctrl+U  scroll half page down / up
{ / }           previous / next paragraph
```

## Editing

```
d + motion      delete (dd = delete line, dw = delete word, d$ = delete to end)
c + motion      change (like delete but enters insert mode)
y + motion      yank (copy)
p               paste after cursor
u               undo
Ctrl+R          redo
.               repeat last command
```

## Search and Replace

```
/pattern        search forward
?pattern        search backward
n / N           next / previous match
:%s/old/new/g   replace all in file
:%s/old/new/gc  replace with confirmation
```

## File Operations

```
:w              save
:q              quit
:wq             save and quit
:q!             quit without saving
:e filename     open file
:split file     horizontal split
:vsplit file    vertical split
Ctrl+W + hjkl   navigate between splits
```

## .vimrc Essentials

```vim
set number          " line numbers
set relativenumber  " relative line numbers (great for d3j type commands)
set tabstop=4
set expandtab       " spaces instead of tabs
set hlsearch        " highlight search results
set incsearch       " incremental search
syntax on
```

## See Also

[[Linux_Commands]] for shell context, [[Bash_Scripting]] for scripting alongside Vim editing.
