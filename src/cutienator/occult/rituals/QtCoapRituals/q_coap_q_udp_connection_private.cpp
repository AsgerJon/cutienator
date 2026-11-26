//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/6.12.0/QtCoap/private/qcoapqudpconnection_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCoap/QtCoap>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/6.12.0/QtCoap/private/qcoapqudpconnection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCoap/qcoapsecurityconfiguration.h>
#include <QtNetwork/qnetworkdatagram.h>
#include <cstring>
#include <optional>
#include <QtNetwork/QNetworkDatagram>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/private/qcoapconnection_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtCoap/private/qcoapqudpconnection_p.h>
#include <QtCoap/private/qcoapnamespace_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtNetwork/qnetworkdatagram.h>
#include <QtNetwork/private/qabstractsocket_p.h>
#if QT_CONFIG(dtls)
#include <QtNetwork/QDtls>
#include <QtNetwork/QSslPreSharedKeyAuthenticator>
#include <QtNetwork/QSslConfiguration>
#include <QtNetwork/QSslKey>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcoap/src/coap/qcoapconnection.cpp, line 119, as _ZN22QCoapConnectionPrivateC2EN6QtCoap12SecurityModeE
inline QCoapConnectionPrivate::QCoapConnectionPrivate(QtCoap::SecurityMode security)
    : securityMode(security)
    , state(QCoapConnection::ConnectionState::Unconnected)
{}

//  from ../qtcoap/src/coap/qcoapqudpconnection.cpp, line 161, as _ZN26QCoapQUdpConnectionPrivate4bindEv
inline bool QCoapQUdpConnectionPrivate::bind()
{
#if QT_CONFIG(networkinterface)
    // Using the QAbstractSocketPrivate private API to bind to a specific
    // network interface.
    auto priv = static_cast<QAbstractSocketPrivate *>(QObjectPrivate::get(socket()));
    QNetworkInterface *iface = udpNetworkInterface.isValid() ? &udpNetworkInterface : nullptr;
    return priv->bind(QHostAddress::Any, 0, QAbstractSocket::ShareAddress, iface);
#else
    return socket()->bind(QHostAddress::Any, 0, QAbstractSocket::ShareAddress);
#endif
}

//  from ../qtcoap/src/coap/qcoapqudpconnection.cpp, line 146, as _ZN26QCoapQUdpConnectionPrivateD2Ev
inline QCoapQUdpConnectionPrivate::~QCoapQUdpConnectionPrivate()
{
#if QT_CONFIG(dtls)
    if (dtls && dtls->isConnectionEncrypted()) {
        Q_ASSERT(udpSocket);
        dtls->shutdown(udpSocket);
    }
#endif
}

//  from ../qtcoap/src/coap/qcoapconnection.cpp, line 11, as _Z16lcCoapConnectionv
inline const QLoggingCategory &lcCoapConnection()
{
    static const QLoggingCategory category("qt.coap.connection");
    return category;
}

//  from ../qtcoap/src/coap/qcoapconnection.cpp, line 189, as _ZNK15QCoapConnection8isSecureEv
inline bool QCoapConnection::isSecure() const
{
    Q_D(const QCoapConnection);
    return d->securityMode != QtCoap::SecurityMode::NoSecurity;
}

//  from ../qtcoap/src/coap/qcoapqudpconnection.cpp, line 271, as _ZN26QCoapQUdpConnectionPrivate13writeToSocketERK10QByteArrayRK7QStringt
inline void QCoapQUdpConnectionPrivate::writeToSocket(const QByteArray &data, const QString &host, quint16 port)
{
#if QT_CONFIG(dtls)
    Q_Q(QCoapQUdpConnection);
#endif
    if (!socket()->isWritable()) {
        bool opened = socket()->open(socket()->openMode() | QIODevice::WriteOnly);
        if (!opened) {
            qCWarning(lcCoapConnection, "Failed to open the UDP socket with write permission");
            return;
        }
    }

    QHostAddress hostAddress(host);
    if (hostAddress.isNull()) {
        qCWarning(lcCoapConnection) << "Invalid host IP address" << host
                                    << "- only IPv4/IPv6 destination addresses are supported.";
        return;
    }

    const qint64 bytesWritten =
#if QT_CONFIG(dtls)
            q->isSecure() ? (Q_ASSERT(dtls), dtls->writeDatagramEncrypted(socket(), data)) :
#endif
            socket()->writeDatagram(data, hostAddress, port);

    if (bytesWritten < 0)
        qCWarning(lcCoapConnection) << "Failed to write datagram:" << socket()->errorString();
}

//  from ../qtcoap/src/coap/qcoapqudpconnection.cpp, line 348, as _ZN26QCoapQUdpConnectionPrivate24setSecurityConfigurationERK26QCoapSecurityConfiguration
inline void QCoapQUdpConnectionPrivate::setSecurityConfiguration(
        const QCoapSecurityConfiguration &configuration)
{
#if QT_CONFIG(dtls)
    Q_ASSERT(dtls);
    auto dtlsConfig = dtls->dtlsConfiguration();

    if (!configuration.defaultCipherString().isEmpty()) {
        dtlsConfig.setBackendConfigurationOption("CipherString",
                                                 configuration.defaultCipherString());
    }

    if (!configuration.caCertificates().isEmpty())
        dtlsConfig.setCaCertificates(configuration.caCertificates().toList());

    if (!configuration.localCertificateChain().isEmpty())
        dtlsConfig.setLocalCertificateChain(configuration.localCertificateChain().toList());

    if (!configuration.privateKey().isNull()) {
        if (configuration.privateKey().algorithm() != QSsl::Opaque) {
            QSslKey privateKey(configuration.privateKey().key(),
                               configuration.privateKey().algorithm(),
                               configuration.privateKey().encodingFormat(),
                               QSsl::PrivateKey,
                               configuration.privateKey().passPhrase());
            dtlsConfig.setPrivateKey(privateKey);
        } else if (configuration.privateKey().handle()) {
            QSslKey opaqueKey(configuration.privateKey().handle());
            dtlsConfig.setPrivateKey(opaqueKey);
        } else {
            qCWarning(lcCoapConnection, "Failed to set private key, the provided key is invalid");
        }
    }

    dtls->setDtlsConfiguration(dtlsConfig);
#else
    Q_UNUSED(configuration);
#endif
}

//  from ../qtcoap/src/coap/qcoapqudpconnection.cpp, line 393, as _ZNK26QCoapQUdpConnectionPrivate31datagramMatchesNetworkInterfaceERK16QNetworkDatagram
inline bool QCoapQUdpConnectionPrivate::datagramMatchesNetworkInterface(
        const QNetworkDatagram &datagram) const
{
#if QT_CONFIG(networkinterface)
    return !udpNetworkInterface.isValid()
            || uint(udpNetworkInterface.index()) == datagram.interfaceIndex();
#else
    Q_UNUSED(datagram);
    return true;
#endif
}

//  from ../qtcoap/src/coap/qcoapqudpconnection.cpp, line 442, as _ZNK26QCoapQUdpConnectionPrivate24receiveDatagramDecryptedEv
#if QT_CONFIG(dtls)
inline std::optional<QNetworkDatagram> QCoapQUdpConnectionPrivate::receiveDatagramDecrypted() const
{
    auto datagram = socket()->receiveDatagram();
    if (!datagramMatchesNetworkInterface(datagram))
        return std::nullopt;

    const QByteArray plainText = dtls->decryptDatagram(socket(), datagram.data());
    datagram.setData(plainText);
    return datagram;
}
#endif  // QT_CONFIG(dtls)
//  -----------------------------------------------------------------------

//  A QCoapQUdpConnectionPrivate that Python can take functions over in. Every QCoapQUdpConnectionPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQCoapQUdpConnectionPrivateCall0)(const void *, int *);
class CuteQCoapQUdpConnectionPrivate : public QCoapQUdpConnectionPrivate {
public:
  using QCoapQUdpConnectionPrivate::QCoapQUdpConnectionPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN26QCoapQUdpConnectionPrivate4bindEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  bool QCoapQUdpConnectionPrivate::bind()
  bool bind() override {
    if (taken[0]) {
      int handled = 0;
      CuteQCoapQUdpConnectionPrivateCall0 call = reinterpret_cast<CuteQCoapQUdpConnectionPrivateCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCoapQUdpConnectionPrivate::bind();
  }
};

//  QCoapQUdpConnectionPrivate::~QCoapQUdpConnectionPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCoapQUdpConnectionPrivateD1Ev(
    QCoapQUdpConnectionPrivate *self) {
  delete self;
}

//  bool QCoapQUdpConnectionPrivate::bind()
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QCoapQUdpConnectionPrivate4bindEv(
    QCoapQUdpConnectionPrivate *self) {
  return self->bind();
}

//  void QCoapQUdpConnectionPrivate::writeToSocket(const QByteArray &data,
//      const QString &host, quint16 port)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCoapQUdpConnectionPrivate13writeToSocketERK10QByteArrayRK7QStringt(
    QCoapQUdpConnectionPrivate *self,
    const QByteArray *data,
    const QString *host,
    quint16 port) {
  self->writeToSocket(*data, *host, port);
}

//  QUdpSocket *QCoapQUdpConnectionPrivate::socket() const
extern "C" Q_DECL_EXPORT
QUdpSocket *ritual_ZNK26QCoapQUdpConnectionPrivate6socketEv(
    const QCoapQUdpConnectionPrivate *self) {
  return self->socket();
}

//  void QCoapQUdpConnectionPrivate::setSecurityConfiguration(const
//      QCoapSecurityConfiguration &configuration)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCoapQUdpConnectionPrivate24setSecurityConfigurationERK26QCoapSecurityConfiguration(
    QCoapQUdpConnectionPrivate *self,
    const QCoapSecurityConfiguration *configuration) {
  self->setSecurityConfiguration(*configuration);
}

//  bool QCoapQUdpConnectionPrivate::datagramMatchesNetworkInterface(const
//      QNetworkDatagram &datagram) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QCoapQUdpConnectionPrivate31datagramMatchesNetworkInterfaceERK16QNetworkDatagram(
    const QCoapQUdpConnectionPrivate *self,
    const QNetworkDatagram *datagram) {
  return self->datagramMatchesNetworkInterface(*datagram);
}

#if QT_CONFIG(dtls)
//  std::optional<QNetworkDatagram>
//      QCoapQUdpConnectionPrivate::receiveDatagramDecrypted() const
extern "C" Q_DECL_EXPORT
std::optional<QNetworkDatagram> *ritual_ZNK26QCoapQUdpConnectionPrivate24receiveDatagramDecryptedEv(
    const QCoapQUdpConnectionPrivate *self) {
  return new std::optional<QNetworkDatagram>(
      self->receiveDatagramDecrypted());
}
#endif  // QT_CONFIG(dtls)

//  QCoapQUdpConnection *QCoapQUdpConnectionPrivate::q_func()
extern "C" Q_DECL_EXPORT
QCoapQUdpConnection *ritual_ZN26QCoapQUdpConnectionPrivate6q_funcEv(
    QCoapQUdpConnectionPrivate *self) {
  return self->q_func();
}

//  const QCoapQUdpConnection *QCoapQUdpConnectionPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QCoapQUdpConnection *ritual_ZNK26QCoapQUdpConnectionPrivate6q_funcEv(
    const QCoapQUdpConnectionPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQCoapQUdpConnectionPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCoapQUdpConnectionPrivate(
    QCoapQUdpConnectionPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCoapQUdpConnectionPrivate *>(self)->take(key, call);
}

//  bool QCoapQUdpConnectionPrivate::bind()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN26QCoapQUdpConnectionPrivate4bindEv(
    QCoapQUdpConnectionPrivate *self) {
  return self->QCoapQUdpConnectionPrivate::bind();
}

//  a std::optional<QNetworkDatagram> a ritual of QCoapQUdpConnectionPrivate
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QCoapQUdpConnectionPrivate__std_optional_QNetworkDatagram(
    std::optional<QNetworkDatagram> *self) {
  delete self;
}
