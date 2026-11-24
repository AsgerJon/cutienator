//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qnetworkproxy.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if !defined(QT_NO_NETWORKPROXY)
#include <QtNetwork/qnetworkproxy.h>
#include <QtCore/qlist.h>

//  QNetworkProxyFactory::~QNetworkProxyFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QNetworkProxyFactoryD1Ev(QNetworkProxyFactory *self) {
  delete self;
}

//  QList<QNetworkProxy> QNetworkProxyFactory::queryProxy(const
//      QNetworkProxyQuery &query)
extern "C" Q_DECL_EXPORT
QList<QNetworkProxy> *ritual_ZN20QNetworkProxyFactory10queryProxyERK18QNetworkProxyQuery(
    QNetworkProxyFactory *self,
    const QNetworkProxyQuery *query) {
  return new QList<QNetworkProxy>(self->queryProxy(*query));
}

//  bool QNetworkProxyFactory::usesSystemConfiguration()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QNetworkProxyFactory23usesSystemConfigurationEv() {
  return QNetworkProxyFactory::usesSystemConfiguration();
}

//  void QNetworkProxyFactory::setUseSystemConfiguration(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QNetworkProxyFactory25setUseSystemConfigurationEb(
    bool enable) {
  QNetworkProxyFactory::setUseSystemConfiguration(enable);
}

//  void
//      QNetworkProxyFactory::setApplicationProxyFactory(QNetworkProxyFactory
//      *factory)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QNetworkProxyFactory26setApplicationProxyFactoryEPS_(
    QNetworkProxyFactory *factory) {
  QNetworkProxyFactory::setApplicationProxyFactory(factory);
}

//  QList<QNetworkProxy> QNetworkProxyFactory::proxyForQuery(const
//      QNetworkProxyQuery &query)
extern "C" Q_DECL_EXPORT
QList<QNetworkProxy> *ritual_ZN20QNetworkProxyFactory13proxyForQueryERK18QNetworkProxyQuery(
    const QNetworkProxyQuery *query) {
  return new QList<QNetworkProxy>(
      QNetworkProxyFactory::proxyForQuery(
          *query));
}

//  QList<QNetworkProxy> QNetworkProxyFactory::systemProxyForQuery(const
//      QNetworkProxyQuery &query)
extern "C" Q_DECL_EXPORT
QList<QNetworkProxy> *ritual_ZN20QNetworkProxyFactory19systemProxyForQueryERK18QNetworkProxyQuery(
    const QNetworkProxyQuery *query) {
  return new QList<QNetworkProxy>(
      QNetworkProxyFactory::systemProxyForQuery(
          *query));
}

#endif  // !defined(QT_NO_NETWORKPROXY)
