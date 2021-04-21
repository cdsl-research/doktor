docker build -t takahyon/doktor-web service/website
docker push takahyon/doktor-web

docker build -t takahyon/doktor-upload service/upload
docker push takahyon/doktor-upload

docker build -t takahyon/doktor-search service/search
docker push takahyon/doktor-search