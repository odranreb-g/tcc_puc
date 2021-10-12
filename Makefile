create_cluster:
	kind create cluster --config=./infra/kind/kindconfig.yaml
	kubectl apply -f ./infra/kind/contour.yaml
	kubectl patch daemonsets -n projectcontour envoy -p '{"spec":{"template":{"spec":{"nodeSelector":{"ingress-ready":"true"},"tolerations":[{"key":"node-role.kubernetes.io/master","operator":"Equal","effect":"NoSchedule"}]}}}}'

build_and_load_images:
	cd projects/deliveries_api && \
	docker build . -t tcc_deliveries_api:0.0.8 && \
	kind load docker-image tcc_deliveries_api:0.0.8 && \
	cd -

	cd projects/partner_routes_api && \
	docker build . -t tcc_partner_routes_api:0.0.7 && \
	kind load docker-image tcc_partner_routes_api:0.0.7 && \
	cd -

	cd projects/legacy_system && \
	docker build . -t tcc_legacy_system:0.0.5 && \
	kind load docker-image tcc_legacy_system:0.0.5 && \
	cd -

	cd projects/pooling_system && \
	docker build . -t tcc_pooling_system:0.0.4 && \
	kind load docker-image tcc_pooling_system:0.0.4 && \
	cd -

	cd projects/new_partner_routes_service && \
	docker build . -t tcc_new_partner_routes_service:0.0.2 && \
	kind load docker-image tcc_new_partner_routes_service:0.0.2 && \
	cd -

	cd projects/pool_partner_price_service && \
	docker build . -t tcc_pool_partner_price_service:0.0.2 && \
	kind load docker-image tcc_pool_partner_price_service:0.0.2 && \
	cd -

	cd projects/zpl_generate_service && \
	docker build . -t tcc_zpl_generate_service:0.0.2 && \
	kind load docker-image tcc_zpl_generate_service:0.0.2 && \
	cd -