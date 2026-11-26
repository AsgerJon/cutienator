//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebSockets/6.12.0/QtWebSockets/private/qwebsockethandshakeresponse_p.h,
//  Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QWebSocketHandshakeResponse' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  2 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtWebSockets/QtWebSockets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebSockets/6.12.0/QtWebSockets/private/qwebsockethandshakeresponse_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtWebSockets/private/qwebsockethandshakeresponse_p.h>
#include <QtWebSockets/private/qwebsockethandshakerequest_p.h>
#include <QtWebSockets/qwebsocketprotocol.h>
#include <QtWebSockets/private/qwebsocketprotocol_p.h>
#include <QtCore/QString>
#include <QtCore/QTextStream>
#include <QtCore/QByteArray>
#include <QtCore/QStringList>
#include <QtCore/QDateTime>
#include <QtCore/QLocale>
#include <QtCore/QCryptographicHash>
#include <QtCore/QSet>
#include <QtCore/QList>
#include <QtCore/QStringBuilder>   //for more efficient string concatenation
#include <algorithm>
#include <functional>   //for std::greater
#include <iterator>
#include <QtWebSockets/private/qwebsockethandshakerequest_p.h>
#include <QtWebSockets/qwebsocketprotocol.h>
#include <QtWebSockets/private/qwebsocketprotocol_p.h>
#include <QtCore/QString>
#include <QtCore/QMap>
#include <QtCore/QTextStream>
#include <QtCore/QUrl>
#include <QtCore/QList>
#include <QtCore/QStringList>
#include <functional>   //for std::greater
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 94, as local:qwebsockethandshakeresponse.cpp:listIntersection
template <class T, class Compare>
static QList<T> listIntersection(QList<T> list1, QList<T> list2, Compare comp)
{
    QList<T> result;
    std::sort(list1.begin(), list1.end(), comp);
    std::sort(list2.begin(), list2.end(), comp);
    std::set_intersection(list1.cbegin(), list1.cend(),
                          list2.cbegin(), list2.cend(),
                          std::back_inserter(result), comp);
    return result;
}

//  from QtWebSockets__QWebSocketHandshakeResponse.cpp, line 1, as moc:QWebSocketHandshakeResponse
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN27QWebSocketHandshakeResponseE_t {};
} // unnamed namespace

template <> constexpr inline auto QWebSocketHandshakeResponse::qt_create_metaobjectdata<qt_meta_tag_ZN27QWebSocketHandshakeResponseE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QWebSocketHandshakeResponse"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QWebSocketHandshakeResponse, qt_meta_tag_ZN27QWebSocketHandshakeResponseE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QWebSocketHandshakeResponse::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN27QWebSocketHandshakeResponseE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN27QWebSocketHandshakeResponseE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN27QWebSocketHandshakeResponseE_t>.metaTypes,
    nullptr
} };

void QWebSocketHandshakeResponse::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QWebSocketHandshakeResponse *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QWebSocketHandshakeResponse::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QWebSocketHandshakeResponse::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN27QWebSocketHandshakeResponseE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QWebSocketHandshakeResponse::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 55, as _ZN27QWebSocketHandshakeResponseD0Ev
inline QWebSocketHandshakeResponse::~QWebSocketHandshakeResponse()
{
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 109, as _ZN27QWebSocketHandshakeResponse20getHandshakeResponseERK26QWebSocketHandshakeRequestRK7QStringbRK5QListIN18QWebSocketProtocol7VersionEERKS6_IS3_ESE_
inline QString QWebSocketHandshakeResponse::getHandshakeResponse(
        const QWebSocketHandshakeRequest &request,
        const QString &serverName,
        bool isOriginAllowed,
        const QList<QWebSocketProtocol::Version> &supportedVersions,
        const QList<QString> &supportedProtocols,
        const QList<QString> &supportedExtensions)
{
    QStringList response;
    m_canUpgrade = false;

    if (!isOriginAllowed) {
        if (!m_canUpgrade) {
            m_error = QWebSocketProtocol::CloseCodePolicyViolated;
            m_errorString = tr("Access forbidden.");
            response << QStringLiteral("HTTP/1.1 403 Access Forbidden");
        }
    } else {
        if (request.isValid()) {
            const QString acceptKey = calculateAcceptKey(request.key());

            // Find first client protocol that is supported. Order is important!
            const QString protocol = [&] {
                const auto clientProtocols = request.protocols();

                const auto isSupportedProtocol = [&](const QString &protocol) {
                    return supportedProtocols.contains(protocol);
                };
                const auto it = std::find_if(
                            clientProtocols.constBegin(), clientProtocols.constEnd(),
                            isSupportedProtocol);

                return it == clientProtocols.constEnd() ? QString() : *it;
            }();

            //TODO: extensions must be kept in the order in which they arrive
            //cannot use set.intersect() to get the supported extensions
            const QList<QString> matchingExtensions =
                listIntersection(supportedExtensions, request.extensions(),
                                 std::less<QString>());
            const QList<QWebSocketProtocol::Version> matchingVersions =
                listIntersection(supportedVersions, request.versions(),
                                 std::greater<QWebSocketProtocol::Version>()); //sort in descending order

            if (Q_UNLIKELY(matchingVersions.isEmpty())) {
                m_error = QWebSocketProtocol::CloseCodeProtocolError;
                m_errorString = tr("Unsupported version requested.");
                m_canUpgrade = false;
            } else {
                response << QStringLiteral("HTTP/1.1 101 Switching Protocols") <<
                            QStringLiteral("Upgrade: websocket") <<
                            QStringLiteral("Connection: Upgrade") <<
                            QStringLiteral("Sec-WebSocket-Accept: ") % acceptKey;
                if (!protocol.isEmpty()) {
                    m_acceptedProtocol = protocol;
                    response << QStringLiteral("Sec-WebSocket-Protocol: ") % m_acceptedProtocol;
                }
                if (!matchingExtensions.isEmpty()) {
                    m_acceptedExtension = matchingExtensions.first();
                    response << QStringLiteral("Sec-WebSocket-Extensions: ") % m_acceptedExtension;
                }
                QString origin = request.origin().trimmed();
                if (origin.contains(QStringLiteral("\r\n")) ||
                        serverName.contains(QStringLiteral("\r\n"))) {
                    m_error = QWebSocketProtocol::CloseCodeAbnormalDisconnection;
                    m_errorString = tr("One of the headers contains a newline. " \
                                       "Possible attack detected.");
                    m_canUpgrade = false;
                } else {
                    if (origin.isEmpty())
                        origin = QStringLiteral("*");
                    QDateTime datetime = QDateTime::currentDateTimeUtc();
                    if (!serverName.isEmpty())
                        response << QStringLiteral("Server: ") % serverName;
                    response << QStringLiteral("Access-Control-Allow-Credentials: false")    <<
                                QStringLiteral("Access-Control-Allow-Methods: GET")          <<
                                QStringLiteral("Access-Control-Allow-Headers: content-type") <<
                                QStringLiteral("Access-Control-Allow-Origin: ") % origin     <<
                                QStringLiteral("Date: ") % QLocale::c()
                                    .toString(datetime, QStringLiteral("ddd, dd MMM yyyy hh:mm:ss 'GMT'"));


                    m_acceptedVersion = QWebSocketProtocol::currentVersion();
                    m_canUpgrade = true;
                }
            }
        } else {
            m_error = QWebSocketProtocol::CloseCodeProtocolError;
            m_errorString = tr("Bad handshake request received.");
            m_canUpgrade = false;
        }
        if (Q_UNLIKELY(!m_canUpgrade)) {
            response << QStringLiteral("HTTP/1.1 400 Bad Request");
            QStringList versions;
            for (QWebSocketProtocol::Version version : supportedVersions)
                versions << QString::number(static_cast<int>(version));
            response << QStringLiteral("Sec-WebSocket-Version: ")
                                % versions.join(QStringLiteral(", "));
        }
    }
    response << QStringLiteral("\r\n");    //append empty line at end of header
    return response.join(QStringLiteral("\r\n"));
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 151, as _ZNK26QWebSocketHandshakeRequest10extensionsEv
inline QList<QString> QWebSocketHandshakeRequest::extensions() const
{
    return m_extensions;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 119, as _ZNK26QWebSocketHandshakeRequest3keyEv
inline QString QWebSocketHandshakeRequest::key() const
{
    return m_key;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 135, as _ZNK26QWebSocketHandshakeRequest6originEv
inline QString QWebSocketHandshakeRequest::origin() const
{
    return m_origin;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 79, as _ZNK26QWebSocketHandshakeRequest7isValidEv
inline bool QWebSocketHandshakeRequest::isValid() const
{
    return m_isValid;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 103, as _ZNK26QWebSocketHandshakeRequest8versionsEv
inline QList<QWebSocketProtocol::Version> QWebSocketHandshakeRequest::versions() const
{
    return m_versions;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 143, as _ZNK26QWebSocketHandshakeRequest9protocolsEv
inline QList<QString> QWebSocketHandshakeRequest::protocols() const
{
    return m_protocols;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 30, as _ZN27QWebSocketHandshakeResponseC1ERK26QWebSocketHandshakeRequestRK7QStringbRK5QListIN18QWebSocketProtocol7VersionEERKS6_IS3_ESE_
inline QWebSocketHandshakeResponse::QWebSocketHandshakeResponse(
        const QWebSocketHandshakeRequest &request,
        const QString &serverName,
        bool isOriginAllowed,
        const QList<QWebSocketProtocol::Version> &supportedVersions,
        const QList<QString> &supportedProtocols,
        const QList<QString> &supportedExtensions) :
    m_isValid(false),
    m_canUpgrade(false),
    m_response(),
    m_acceptedProtocol(),
    m_acceptedExtension(),
    m_acceptedVersion(QWebSocketProtocol::VersionUnknown),
    m_error(QWebSocketProtocol::CloseCodeNormal),
    m_errorString()
{
    m_response = getHandshakeResponse(request, serverName,
                                      isOriginAllowed, supportedVersions,
                                      supportedProtocols, supportedExtensions);
    m_isValid = true;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 62, as _ZNK27QWebSocketHandshakeResponse7isValidEv
inline bool QWebSocketHandshakeResponse::isValid() const
{
    return m_isValid;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 70, as _ZNK27QWebSocketHandshakeResponse10canUpgradeEv
inline bool QWebSocketHandshakeResponse::canUpgrade() const
{
    return m_isValid && m_canUpgrade;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 78, as _ZNK27QWebSocketHandshakeResponse16acceptedProtocolEv
inline QString QWebSocketHandshakeResponse::acceptedProtocol() const
{
    return m_acceptedProtocol;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 260, as _ZNK27QWebSocketHandshakeResponse17acceptedExtensionEv
inline QString QWebSocketHandshakeResponse::acceptedExtension() const
{
    return m_acceptedExtension;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 236, as _ZNK27QWebSocketHandshakeResponse15acceptedVersionEv
inline QWebSocketProtocol::Version QWebSocketHandshakeResponse::acceptedVersion() const
{
    return m_acceptedVersion;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 244, as _ZNK27QWebSocketHandshakeResponse5errorEv
inline QWebSocketProtocol::CloseCode QWebSocketHandshakeResponse::error() const
{
    return m_error;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 252, as _ZNK27QWebSocketHandshakeResponse11errorStringEv
inline QString QWebSocketHandshakeResponse::errorString() const
{
    return m_errorString;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 86, as _ZNK27QWebSocketHandshakeResponse18calculateAcceptKeyERK7QString
inline QString QWebSocketHandshakeResponse::calculateAcceptKey(const QString &key) const
{
    //the UID comes from RFC6455
    const QString tmpKey = key % QStringLiteral("258EAFA5-E914-47DA-95CA-C5AB0DC85B11");
    const QByteArray hash = QCryptographicHash::hash(tmpKey.toLatin1(), QCryptographicHash::Sha1);
    return QString::fromLatin1(hash.toBase64());
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 216, as _ZNK27QWebSocketHandshakeResponse13writeToStreamER11QTextStream
inline QTextStream &QWebSocketHandshakeResponse::writeToStream(QTextStream &textStream) const
{
    if (Q_LIKELY(!m_response.isEmpty()))
        textStream << m_response.toLatin1().constData();
    else
        textStream.setStatus(QTextStream::WriteFailed);
    return textStream;
}
//  -----------------------------------------------------------------------

//  A QWebSocketHandshakeResponse that Python can take functions over in. Every QWebSocketHandshakeResponse
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebSocketHandshakeResponseCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebSocketHandshakeResponseCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketHandshakeResponseCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketHandshakeResponseCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketHandshakeResponseCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketHandshakeResponseCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketHandshakeResponseCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebSocketHandshakeResponse : public QWebSocketHandshakeResponse {
public:
  using QWebSocketHandshakeResponse::QWebSocketHandshakeResponse;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWebSocketHandshakeResponseCall0 call = reinterpret_cast<CuteQWebSocketHandshakeResponseCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWebSocketHandshakeResponseCall1 call = reinterpret_cast<CuteQWebSocketHandshakeResponseCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWebSocketHandshakeResponseCall2 call = reinterpret_cast<CuteQWebSocketHandshakeResponseCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWebSocketHandshakeResponseCall3 call = reinterpret_cast<CuteQWebSocketHandshakeResponseCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWebSocketHandshakeResponseCall4 call = reinterpret_cast<CuteQWebSocketHandshakeResponseCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWebSocketHandshakeResponseCall5 call = reinterpret_cast<CuteQWebSocketHandshakeResponseCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWebSocketHandshakeResponseCall6 call = reinterpret_cast<CuteQWebSocketHandshakeResponseCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWebSocketHandshakeResponse::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QWebSocketHandshakeResponse10metaObjectEv(
    const QWebSocketHandshakeResponse *self) {
  return self->metaObject();
}

//  void *QWebSocketHandshakeResponse::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QWebSocketHandshakeResponse11qt_metacastEPKc(
    QWebSocketHandshakeResponse *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWebSocketHandshakeResponse::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QWebSocketHandshakeResponse11qt_metacallEN11QMetaObject4CallEiPPv(
    QWebSocketHandshakeResponse *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWebSocketHandshakeResponse::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QWebSocketHandshakeResponse2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebSocketHandshakeResponse::tr(s, c, n));
}

//  QWebSocketHandshakeResponse::QWebSocketHandshakeResponse(const
//      QWebSocketHandshakeRequest &request, const QString &serverName, bool
//      isOriginAllowed, const QList<QWebSocketProtocol::Version>
//      &supportedVersions, const QList<QString> &supportedProtocols, const
//      QList<QString> &supportedExtensions)
extern "C" Q_DECL_EXPORT
QWebSocketHandshakeResponse *ritual_ZN27QWebSocketHandshakeResponseC1ERK26QWebSocketHandshakeRequestRK7QStringbRK5QListIN18QWebSocketProtocol7VersionEERKS6_IS3_ESE_(
    const QWebSocketHandshakeRequest *request,
    const QString *serverName,
    bool isOriginAllowed,
    const QList<QWebSocketProtocol::Version> *supportedVersions,
    const QList<QString> *supportedProtocols,
    const QList<QString> *supportedExtensions) {
  return new CuteQWebSocketHandshakeResponse(
      *request,
      *serverName,
      isOriginAllowed,
      *supportedVersions,
      *supportedProtocols,
      *supportedExtensions);
}

//  QWebSocketHandshakeResponse::~QWebSocketHandshakeResponse()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QWebSocketHandshakeResponseD1Ev(
    QWebSocketHandshakeResponse *self) {
  delete self;
}

//  bool QWebSocketHandshakeResponse::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QWebSocketHandshakeResponse7isValidEv(
    const QWebSocketHandshakeResponse *self) {
  return self->isValid();
}

//  bool QWebSocketHandshakeResponse::canUpgrade() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QWebSocketHandshakeResponse10canUpgradeEv(
    const QWebSocketHandshakeResponse *self) {
  return self->canUpgrade();
}

//  QString QWebSocketHandshakeResponse::acceptedProtocol() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QWebSocketHandshakeResponse16acceptedProtocolEv(
    const QWebSocketHandshakeResponse *self) {
  return new QString(self->acceptedProtocol());
}

//  QString QWebSocketHandshakeResponse::acceptedExtension() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QWebSocketHandshakeResponse17acceptedExtensionEv(
    const QWebSocketHandshakeResponse *self) {
  return new QString(self->acceptedExtension());
}

//  QWebSocketProtocol::Version
//      QWebSocketHandshakeResponse::acceptedVersion() const
extern "C" Q_DECL_EXPORT
QWebSocketProtocol::Version ritual_ZNK27QWebSocketHandshakeResponse15acceptedVersionEv(
    const QWebSocketHandshakeResponse *self) {
  return self->acceptedVersion();
}

//  QWebSocketProtocol::CloseCode QWebSocketHandshakeResponse::error() const
extern "C" Q_DECL_EXPORT
QWebSocketProtocol::CloseCode ritual_ZNK27QWebSocketHandshakeResponse5errorEv(
    const QWebSocketHandshakeResponse *self) {
  return self->error();
}

//  QString QWebSocketHandshakeResponse::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QWebSocketHandshakeResponse11errorStringEv(
    const QWebSocketHandshakeResponse *self) {
  return new QString(self->errorString());
}

//  QString QWebSocketHandshakeResponse::calculateAcceptKey(const QString
//      &key) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QWebSocketHandshakeResponse18calculateAcceptKeyERK7QString(
    const QWebSocketHandshakeResponse *self,
    const QString *key) {
  return new QString(self->calculateAcceptKey(*key));
}

//  QTextStream &QWebSocketHandshakeResponse::writeToStream(QTextStream
//      &textStream) const
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZNK27QWebSocketHandshakeResponse13writeToStreamER11QTextStream(
    const QWebSocketHandshakeResponse *self,
    QTextStream *textStream) {
  return &(self->writeToStream(*textStream));
}

//  a Python function taken by a CuteQWebSocketHandshakeResponse, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebSocketHandshakeResponse(
    QWebSocketHandshakeResponse *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebSocketHandshakeResponse *>(self)->take(key, call);
}
