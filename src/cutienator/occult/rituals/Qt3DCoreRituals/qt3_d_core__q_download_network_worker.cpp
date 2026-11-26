//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qdownloadnetworkworker_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'Qt3DCore::QDownloadNetworkWorker' is pasted in, cut from what the moc of
//  Qt 6.12.0 writes for its header: Qt's library keeps it to itself; added
//  are 2 rituals that lean on what moc writes for a class of the part Qt
//  keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qdownloadnetworkworker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <Qt3DCore/private/qdownloadhelperservice_p.h>
#include <Qt3DCore/private/qdownloadnetworkworker_p.h>
#include <QtNetwork/QNetworkAccessManager>
#include <QtNetwork/QNetworkRequest>
#include <QtNetwork/QNetworkReply>
#include <QtCore/QDataStream>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from Qt3DCore__Qt3DCore_QDownloadNetworkWorker.cpp, line 1, as moc:Qt3DCore::QDownloadNetworkWorker
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN8Qt3DCore22QDownloadNetworkWorkerE_t {};
} // unnamed namespace

template <> constexpr inline auto Qt3DCore::QDownloadNetworkWorker::qt_create_metaobjectdata<qt_meta_tag_ZN8Qt3DCore22QDownloadNetworkWorkerE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "Qt3DCore::QDownloadNetworkWorker",
        "submitRequest",
        "",
        "Qt3DCore::QDownloadRequestPtr",
        "request",
        "cancelRequest",
        "cancelAllRequests",
        "requestDownloaded",
        "onRequestSubmited",
        "onRequestCancelled",
        "onAllRequestsCancelled",
        "onRequestFinished",
        "QNetworkReply*",
        "reply",
        "onDownloadProgressed",
        "bytesReceived",
        "bytesTotal"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'submitRequest'
        QtMocHelpers::SignalData<void(const Qt3DCore::QDownloadRequestPtr &)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 3, 4 },
        }}),
        // Signal 'cancelRequest'
        QtMocHelpers::SignalData<void(const Qt3DCore::QDownloadRequestPtr &)>(5, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 3, 4 },
        }}),
        // Signal 'cancelAllRequests'
        QtMocHelpers::SignalData<void()>(6, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'requestDownloaded'
        QtMocHelpers::SignalData<void(const Qt3DCore::QDownloadRequestPtr &)>(7, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 3, 4 },
        }}),
        // Slot 'onRequestSubmited'
        QtMocHelpers::SlotData<void(const Qt3DCore::QDownloadRequestPtr &)>(8, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { 0x80000000 | 3, 4 },
        }}),
        // Slot 'onRequestCancelled'
        QtMocHelpers::SlotData<void(const Qt3DCore::QDownloadRequestPtr &)>(9, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { 0x80000000 | 3, 4 },
        }}),
        // Slot 'onAllRequestsCancelled'
        QtMocHelpers::SlotData<void()>(10, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'onRequestFinished'
        QtMocHelpers::SlotData<void(QNetworkReply *)>(11, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { 0x80000000 | 12, 13 },
        }}),
        // Slot 'onDownloadProgressed'
        QtMocHelpers::SlotData<void(qint64, qint64)>(14, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { QMetaType::LongLong, 15 }, { QMetaType::LongLong, 16 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QDownloadNetworkWorker, qt_meta_tag_ZN8Qt3DCore22QDownloadNetworkWorkerE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject Qt3DCore::QDownloadNetworkWorker::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN8Qt3DCore22QDownloadNetworkWorkerE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN8Qt3DCore22QDownloadNetworkWorkerE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN8Qt3DCore22QDownloadNetworkWorkerE_t>.metaTypes,
    nullptr
} };

void Qt3DCore::QDownloadNetworkWorker::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QDownloadNetworkWorker *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->submitRequest((*reinterpret_cast<std::add_pointer_t<Qt3DCore::QDownloadRequestPtr>>(_a[1]))); break;
        case 1: _t->cancelRequest((*reinterpret_cast<std::add_pointer_t<Qt3DCore::QDownloadRequestPtr>>(_a[1]))); break;
        case 2: _t->cancelAllRequests(); break;
        case 3: _t->requestDownloaded((*reinterpret_cast<std::add_pointer_t<Qt3DCore::QDownloadRequestPtr>>(_a[1]))); break;
        case 4: _t->onRequestSubmited((*reinterpret_cast<std::add_pointer_t<Qt3DCore::QDownloadRequestPtr>>(_a[1]))); break;
        case 5: _t->onRequestCancelled((*reinterpret_cast<std::add_pointer_t<Qt3DCore::QDownloadRequestPtr>>(_a[1]))); break;
        case 6: _t->onAllRequestsCancelled(); break;
        case 7: _t->onRequestFinished((*reinterpret_cast<std::add_pointer_t<QNetworkReply*>>(_a[1]))); break;
        case 8: _t->onDownloadProgressed((*reinterpret_cast<std::add_pointer_t<qint64>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<qint64>>(_a[2]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        switch (_id) {
        default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
        case 0:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< Qt3DCore::QDownloadRequestPtr >(); break;
            }
            break;
        case 1:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< Qt3DCore::QDownloadRequestPtr >(); break;
            }
            break;
        case 3:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< Qt3DCore::QDownloadRequestPtr >(); break;
            }
            break;
        case 4:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< Qt3DCore::QDownloadRequestPtr >(); break;
            }
            break;
        case 5:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< Qt3DCore::QDownloadRequestPtr >(); break;
            }
            break;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QDownloadNetworkWorker::*)(const Qt3DCore::QDownloadRequestPtr & )>(_a, &QDownloadNetworkWorker::submitRequest, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QDownloadNetworkWorker::*)(const Qt3DCore::QDownloadRequestPtr & )>(_a, &QDownloadNetworkWorker::cancelRequest, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (QDownloadNetworkWorker::*)()>(_a, &QDownloadNetworkWorker::cancelAllRequests, 2))
            return;
        if (QtMocHelpers::indexOfMethod<void (QDownloadNetworkWorker::*)(const Qt3DCore::QDownloadRequestPtr & )>(_a, &QDownloadNetworkWorker::requestDownloaded, 3))
            return;
    }
}

const QMetaObject *Qt3DCore::QDownloadNetworkWorker::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *Qt3DCore::QDownloadNetworkWorker::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN8Qt3DCore22QDownloadNetworkWorkerE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int Qt3DCore::QDownloadNetworkWorker::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 9)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 9;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 9)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 9;
    }
    return _id;
}

// SIGNAL 0
void Qt3DCore::QDownloadNetworkWorker::submitRequest(const Qt3DCore::QDownloadRequestPtr & _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1);
}

// SIGNAL 1
void Qt3DCore::QDownloadNetworkWorker::cancelRequest(const Qt3DCore::QDownloadRequestPtr & _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 1, nullptr, _t1);
}

// SIGNAL 2
void Qt3DCore::QDownloadNetworkWorker::cancelAllRequests()
{
    QMetaObject::activate(this, &staticMetaObject, 2, nullptr);
}

// SIGNAL 3
void Qt3DCore::QDownloadNetworkWorker::requestDownloaded(const Qt3DCore::QDownloadRequestPtr & _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 3, nullptr, _t1);
}
QT_WARNING_POP

//  from ../qt3d/src/core/services/qdownloadnetworkworker.cpp, line 65, as _ZN8Qt3DCore22QDownloadNetworkWorker17onRequestFinishedEP13QNetworkReply
namespace Qt3DCore {
inline void QDownloadNetworkWorker::onRequestFinished(QNetworkReply *reply)
{
    QMutexLocker l(&m_mutex);
    auto it = std::find_if(m_requests.begin(), m_requests.end(),
                           [reply](QPair<QDownloadRequestPtr, QNetworkReply *> e) {
                                        return e.second == reply;
                            });
    if (it == m_requests.end())
        return;

    auto request = (*it).first;
    if (reply->error() == QNetworkReply::NoError) {
        request->m_succeeded = true;
    }
    request->onDownloaded();
    emit requestDownloaded(request);

    m_requests.erase(it);
}
}  // namespace Qt3DCore

//  from ../qt3d/src/core/services/qdownloadnetworkworker.cpp, line 28, as _ZN8Qt3DCore22QDownloadNetworkWorker17onRequestSubmitedERK14QSharedPointerINS_16QDownloadRequestEE
namespace Qt3DCore {
inline void QDownloadNetworkWorker::onRequestSubmited(const QDownloadRequestPtr &request)
{
    QMutexLocker l(&m_mutex);
    if (!m_networkManager) {
        m_networkManager = new QNetworkAccessManager(this);
        connect(m_networkManager, &QNetworkAccessManager::finished,
                  this, &QDownloadNetworkWorker::onRequestFinished);
    }
    auto reply = m_networkManager->get(QNetworkRequest(request->url()));
    m_requests << QPair<QDownloadRequestPtr, QNetworkReply *>(request, reply);
    connect(reply, &QNetworkReply::downloadProgress, this, &QDownloadNetworkWorker::onDownloadProgressed);
}
}  // namespace Qt3DCore

//  from ../qt3d/src/core/services/qdownloadnetworkworker.cpp, line 41, as _ZN8Qt3DCore22QDownloadNetworkWorker18onRequestCancelledERK14QSharedPointerINS_16QDownloadRequestEE
namespace Qt3DCore {
inline void QDownloadNetworkWorker::onRequestCancelled(const QDownloadRequestPtr &request)
{
    QMutexLocker l(&m_mutex);
    auto it = std::find_if(m_requests.begin(), m_requests.end(),
                           [request](QPair<QDownloadRequestPtr, QNetworkReply *> e) {
                                        return e.first == request;
                            });
    if (it == m_requests.end())
        return;

    (*it).first->m_cancelled = true;
    (*it).second->abort();
}
}  // namespace Qt3DCore

//  from ../qt3d/src/core/services/qdownloadnetworkworker.cpp, line 85, as _ZN8Qt3DCore22QDownloadNetworkWorker20onDownloadProgressedExx
namespace Qt3DCore {
inline void QDownloadNetworkWorker::onDownloadProgressed(qint64 bytesReceived, qint64 bytesTotal)
{
    Q_UNUSED(bytesReceived);
    Q_UNUSED(bytesTotal);
    // TODO forward progress details somewhere

    QNetworkReply *reply = qobject_cast<QNetworkReply *>(sender());
    if (!reply)
        return;

    QMutexLocker l(&m_mutex);
    auto it = std::find_if(m_requests.begin(), m_requests.end(),
                           [reply](QPair<QDownloadRequestPtr, QNetworkReply *> e) {
                                        return e.second == reply;
                            });
    if (it == m_requests.end())
        return;

    auto request = (*it).first;
    QDataStream stream(&request->m_data, QIODevice::Append);
    QByteArray data = reply->readAll();
    stream.writeRawData(data.data(), data.size());
}
}  // namespace Qt3DCore

//  from ../qt3d/src/core/services/qdownloadnetworkworker.cpp, line 55, as _ZN8Qt3DCore22QDownloadNetworkWorker22onAllRequestsCancelledEv
namespace Qt3DCore {
inline void QDownloadNetworkWorker::onAllRequestsCancelled()
{
    QMutexLocker l(&m_mutex);
    for (auto &e: std::as_const(m_requests)) {
        e.first->m_cancelled = true;
        e.second->abort();
    }
    m_requests.clear();
}
}  // namespace Qt3DCore

//  from ../qt3d/src/core/services/qdownloadnetworkworker.cpp, line 16, as _ZN8Qt3DCore22QDownloadNetworkWorkerC1EP7QObject
namespace Qt3DCore {
inline QDownloadNetworkWorker::QDownloadNetworkWorker(QObject *parent)
    : QObject(parent)
    , m_networkManager(nullptr)
{
    connect(this, &QDownloadNetworkWorker::submitRequest,
            this, &QDownloadNetworkWorker::onRequestSubmited);
    connect(this, &QDownloadNetworkWorker::cancelRequest,
            this, &QDownloadNetworkWorker::onRequestCancelled);
    connect(this, &QDownloadNetworkWorker::cancelAllRequests,
            this, &QDownloadNetworkWorker::onAllRequestsCancelled);
}
}  // namespace Qt3DCore
//  -----------------------------------------------------------------------

//  const QMetaObject *Qt3DCore::QDownloadNetworkWorker::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore22QDownloadNetworkWorker10metaObjectEv(
    const Qt3DCore::QDownloadNetworkWorker *self) {
  return self->metaObject();
}

//  void *Qt3DCore::QDownloadNetworkWorker::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore22QDownloadNetworkWorker11qt_metacastEPKc(
    Qt3DCore::QDownloadNetworkWorker *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::QDownloadNetworkWorker::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore22QDownloadNetworkWorker11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::QDownloadNetworkWorker *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::QDownloadNetworkWorker::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore22QDownloadNetworkWorker2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::QDownloadNetworkWorker::tr(s, c, n));
}

//  Qt3DCore::QDownloadNetworkWorker::QDownloadNetworkWorker(QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::QDownloadNetworkWorker *ritual_ZN8Qt3DCore22QDownloadNetworkWorkerC1EP7QObject(
    QObject *parent) {
  return new Qt3DCore::QDownloadNetworkWorker(parent);
}

//  void Qt3DCore::QDownloadNetworkWorker::submitRequest(const
//      Qt3DCore::QDownloadRequestPtr &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QDownloadNetworkWorker13submitRequestERK14QSharedPointerINS_16QDownloadRequestEE(
    Qt3DCore::QDownloadNetworkWorker *self,
    const Qt3DCore::QDownloadRequestPtr *request) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DCore::QDownloadNetworkWorker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "submitRequest(const Qt3DCore::QDownloadRequestPtr &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "submitRequest(const Qt3DCore::QDownloadRequestPtr &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(request)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DCore::QDownloadNetworkWorker::cancelRequest(const
//      Qt3DCore::QDownloadRequestPtr &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QDownloadNetworkWorker13cancelRequestERK14QSharedPointerINS_16QDownloadRequestEE(
    Qt3DCore::QDownloadNetworkWorker *self,
    const Qt3DCore::QDownloadRequestPtr *request) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DCore::QDownloadNetworkWorker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "cancelRequest(const Qt3DCore::QDownloadRequestPtr &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "cancelRequest(const Qt3DCore::QDownloadRequestPtr &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(request)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DCore::QDownloadNetworkWorker::cancelAllRequests()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QDownloadNetworkWorker17cancelAllRequestsEv(
    Qt3DCore::QDownloadNetworkWorker *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DCore::QDownloadNetworkWorker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "cancelAllRequests()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "cancelAllRequests()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DCore::QDownloadNetworkWorker::requestDownloaded(const
//      Qt3DCore::QDownloadRequestPtr &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QDownloadNetworkWorker17requestDownloadedERK14QSharedPointerINS_16QDownloadRequestEE(
    Qt3DCore::QDownloadNetworkWorker *self,
    const Qt3DCore::QDownloadRequestPtr *request) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DCore::QDownloadNetworkWorker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "requestDownloaded(const Qt3DCore::QDownloadRequestPtr &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "requestDownloaded(const Qt3DCore::QDownloadRequestPtr &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(request)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DCore::QDownloadNetworkWorker::onRequestSubmited(const
//      Qt3DCore::QDownloadRequestPtr &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QDownloadNetworkWorker17onRequestSubmitedERK14QSharedPointerINS_16QDownloadRequestEE(
    Qt3DCore::QDownloadNetworkWorker *self,
    const Qt3DCore::QDownloadRequestPtr *request) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DCore::QDownloadNetworkWorker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onRequestSubmited(const Qt3DCore::QDownloadRequestPtr &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onRequestSubmited(const Qt3DCore::QDownloadRequestPtr &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(request)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DCore::QDownloadNetworkWorker::onRequestCancelled(const
//      Qt3DCore::QDownloadRequestPtr &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QDownloadNetworkWorker18onRequestCancelledERK14QSharedPointerINS_16QDownloadRequestEE(
    Qt3DCore::QDownloadNetworkWorker *self,
    const Qt3DCore::QDownloadRequestPtr *request) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DCore::QDownloadNetworkWorker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onRequestCancelled(const Qt3DCore::QDownloadRequestPtr &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onRequestCancelled(const Qt3DCore::QDownloadRequestPtr &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(request)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DCore::QDownloadNetworkWorker::onAllRequestsCancelled()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QDownloadNetworkWorker22onAllRequestsCancelledEv(
    Qt3DCore::QDownloadNetworkWorker *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DCore::QDownloadNetworkWorker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onAllRequestsCancelled()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onAllRequestsCancelled()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DCore::QDownloadNetworkWorker::onRequestFinished(QNetworkReply
//      *reply)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QDownloadNetworkWorker17onRequestFinishedEP13QNetworkReply(
    Qt3DCore::QDownloadNetworkWorker *self,
    QNetworkReply *reply) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DCore::QDownloadNetworkWorker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onRequestFinished(QNetworkReply *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onRequestFinished(QNetworkReply *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&reply)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DCore::QDownloadNetworkWorker::onDownloadProgressed(qint64
//      bytesReceived, qint64 bytesTotal)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QDownloadNetworkWorker20onDownloadProgressedExx(
    Qt3DCore::QDownloadNetworkWorker *self,
    qint64 bytesReceived,
    qint64 bytesTotal) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DCore::QDownloadNetworkWorker")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onDownloadProgressed(qint64,qint64)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onDownloadProgressed(qint64,qint64)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&bytesReceived)),
      const_cast<void *>(static_cast<const void *>(&bytesTotal)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
