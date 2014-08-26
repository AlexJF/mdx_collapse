######################################
Collapse Extension for Python-Markdown
######################################

Allow the definition of collapsible blocks in Markdown.

Generated code is designed for compatibility with `Bootstrap
<http://getbootstrap.com/>`_.

Based on the official Admonition extension.

Usage
=====

Blocks starting with ``<<<`` will start collapsed, blocks
starting with ``>>>`` will start uncollapsed.

Syntax: ::

    <<< [<Panel Id>] "<Panel Title>"
        Paragraph1

        Paragraph2

or ::

    >>> [<Panel Id>] "<Panel Title>"
        Paragraph1

        Paragraph2

Example
=======

::

    <<< "Collapsible stuff"
        * Stuff 1
        * Stuff 2
        * Stuff 3
        * Stuff 4

becomes

.. code-block:: html

    <div class="panel panel-default panel-collapsible">
        <div class="panel-heading">
            <a data-toggle="collapse" data-target="#collapse1" />
        </div>
        <div id="collapse1" class="panel-body collapse in">
            <ul>
                <li>Stuff 1</li>
                <li>Stuff 2</li>
                <li>Stuff 3</li>
                <li>Stuff 4</li>
            </ul>
        </div>
    </div>
