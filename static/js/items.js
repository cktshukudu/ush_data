const Ip = document.getElementById('Ip');
const server = document.getElementById('server');
const owner = document.getElementById('owner');
const loc = document.getElementById('loc');
const manu = document.getElementById('manu');
const model = document.getElementById('model');

const addMore = document.getElementById('addMore');
const removeFields = document.getElementById('removeFields');
addMore.onclick = function () {
            const newIp = document.createElement('input');
            newIp.setAttribute('type', 'text');
            newIp.setAttribute('name', 'Ip');
            newIp.setAttribute('placeholder', 'Ip Address')
            Ip.appendChild(newIp);

            const newServer = document.createElement('input');
            newServer.setAttribute('type', 'text');
            newServer.setAttribute('name', 'server');
            newServer.setAttribute('placeholder', 'Server');
            server.appendChild(newServer);

            const newOwner = document.createElement('input');
            newOwner.setAttribute('type', 'text');
            newOwner.setAttribute('name', 'owner');
            newOwner.setAttribute('placeholder', 'Owner');
            owner.appendChild(newOwner);

            const newLoc = document.createElement('input');
            newLoc.setAttribute('type', 'text');
            newLoc.setAttribute('name', 'loc');
            newLoc.setAttribute('placeholder', 'location')
            loc.appendChild(newLoc);

            const newManu = document.createElement('input');
            newManu.setAttribute('type', 'text');
            newManu.setAttribute('name', 'manu');
            newManu.setAttribute('placeholder', 'Manufacturer');
            manu.appendChild(newManu);

            const newModel = document.createElement('input');
            newModel.setAttribute('type', 'text');
            newModel.setAttribute('name', 'model');
            newModel.setAttribute('placeholder', 'Model');
            model.appendChild(newModel);
        };

        removeFields.onclick = function () {
            const IpTag = Ip.getElementsByTagName('input');
            const serverTag = server.getElementsByTagName('input');
            const ownerTag = owner.getElementsByTagName('input');
            const locTag = loc.getElementsByTagName('input');
            const manuTag = manu.getElementsByTagName('input');
            const modelTag = model.getElementsByTagName('input');
            if (IpTag.length > 1) {
                Ip.removeChild(IpTag[(IpTag.length) - 1]);
                server.removeChild(serverTag[(serverTag.length) - 1]);
                owner.removeChild(ownerTag[(ownerTag.length) - 1]);
                loc.removeChild(locTag[(locTag.length) - 1]);
                manu.removeChild(manuTag[(manuTag.length) - 1]);
                model.removeChild(modelTag[(modelTag.length) - 1]);
            };
        }