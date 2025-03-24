<script setup lang="ts">
</script>

<template>
<body>
    <div class="game-description">
        <h1>Escape the Dungeon</h1>
    </div>
    <div class="health" id="health">
        <div class="healthbar" id="healthbar"></div>
    </div>
    <div class="interactions">
        <div class="outcome">
            <textarea disabled=true id="outcome-ta">outcome of your actions...</textarea>
        </div>
        <h2>Action</h2>
        <div>
            <div class="actions" id="all-actions">
                <button id="action-spawn">Spawn Spell</button>
            </div>
        </div>
        <h2>Movement</h2>
        <div class="movements">
            <button id="move-forward" disabled=true>forward</button>
            <button id="move-backward" disabled=true>backward</button>
            <button id="move-left" disabled=true>left</button>
            <button id="move-right" disabled=true>right</button>
        </div>
    </div>
    <div class="bottom-window">
        <div class="inventory">
            <h2>Inventory</h2>
            <div class="items">
                <table id="invTable">
                    <thead>
                        <tr>
                            <th>Items</th>
                            <th>Description</th>
                            <th style="width: 100px;">Use</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                        <td>-</td>
                        <td>-</td>
                        <td>-</td>
                    </tr>
                    <tr>
                        <td>-</td>
                        <td>-</td>
                        <td>-</td>
                    </tr>
                    <tr>
                        <td>-</td>
                        <td>-</td>
                        <td>-</td>
                    </tr>
                    <tr>
                        <td>-</td>
                        <td>-</td>
                        <td>-</td>
                    </tr>
                    <tr>
                        <td>-</td>
                        <td>-</td>
                        <td>-</td>
                    </tr>
                    <tr>
                        <td>-</td>
                        <td>-</td>
                        <td>-</td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="cover">
        </div>
    </div>
</body>
</template>
