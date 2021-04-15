dokcer build -t takahyon/dokter-web service/web
docker push takahyon/dokter-web

dokcer build -t takahyon/dokter-upload service/upload
docker push takahyon/dokter-upload

dokcer build -t takahyon/dokter-search service/search
docker push takahyon/dokter-search