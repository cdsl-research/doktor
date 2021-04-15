docker build -t takahyon/dokter-web service/website
docker push takahyon/dokter-web

docker build -t takahyon/dokter-upload service/upload
docker push takahyon/dokter-upload

docker build -t takahyon/dokter-search service/search
docker push takahyon/dokter-search