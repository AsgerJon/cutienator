//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypeloadernetworkreplyproxy_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QQmlTypeLoaderNetworkReplyProxy' is pasted in, cut from what the moc of
//  Qt 6.12.0 writes for its header: Qt's library keeps it to itself; added
//  are 2 rituals that lean on what moc writes for a class of the part Qt
//  keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if QT_CONFIG(qml_network)
#if QT_CONFIG(qml_network)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypeloadernetworkreplyproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQml/private/qqmltypeloadernetworkreplyproxy_p.h>
#include <QtQml/private/qqmltypeloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQml__QQmlTypeLoaderNetworkReplyProxy.cpp, line 1, as moc:QQmlTypeLoaderNetworkReplyProxy
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN31QQmlTypeLoaderNetworkReplyProxyE_t {};
} // unnamed namespace

template <> constexpr inline auto QQmlTypeLoaderNetworkReplyProxy::qt_create_metaobjectdata<qt_meta_tag_ZN31QQmlTypeLoaderNetworkReplyProxyE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQmlTypeLoaderNetworkReplyProxy",
        "finished",
        "",
        "downloadProgress",
        "manualFinished",
        "QNetworkReply*"
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'finished'
        QtMocHelpers::SlotData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
        // Slot 'downloadProgress'
        QtMocHelpers::SlotData<void(qint64, qint64)>(3, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::LongLong, 2 }, { QMetaType::LongLong, 2 },
        }}),
        // Slot 'manualFinished'
        QtMocHelpers::SlotData<void(QNetworkReply *)>(4, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 5, 2 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QQmlTypeLoaderNetworkReplyProxy, qt_meta_tag_ZN31QQmlTypeLoaderNetworkReplyProxyE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QQmlTypeLoaderNetworkReplyProxy::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN31QQmlTypeLoaderNetworkReplyProxyE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN31QQmlTypeLoaderNetworkReplyProxyE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN31QQmlTypeLoaderNetworkReplyProxyE_t>.metaTypes,
    nullptr
} };

void QQmlTypeLoaderNetworkReplyProxy::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQmlTypeLoaderNetworkReplyProxy *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->finished(); break;
        case 1: _t->downloadProgress((*reinterpret_cast<std::add_pointer_t<qint64>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<qint64>>(_a[2]))); break;
        case 2: _t->manualFinished((*reinterpret_cast<std::add_pointer_t<QNetworkReply*>>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObject *QQmlTypeLoaderNetworkReplyProxy::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQmlTypeLoaderNetworkReplyProxy::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN31QQmlTypeLoaderNetworkReplyProxyE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQmlTypeLoaderNetworkReplyProxy::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 3)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 3)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 3;
    }
    return _id;
}
QT_WARNING_POP

//  from ../qtdeclarative/src/qml/qml/qqmltypeloadernetworkreplyproxy.cpp, line 33, as _ZN31QQmlTypeLoaderNetworkReplyProxy14manualFinishedEP13QNetworkReply
inline void QQmlTypeLoaderNetworkReplyProxy::manualFinished(QNetworkReply *reply)
{
    qint64 replySize = reply->size();
    l->networkReplyProgress(reply, replySize, replySize);
    l->networkReplyFinished(reply);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypeloadernetworkreplyproxy.cpp, line 24, as _ZN31QQmlTypeLoaderNetworkReplyProxy16downloadProgressExx
inline void QQmlTypeLoaderNetworkReplyProxy::downloadProgress(qint64 bytesReceived, qint64 bytesTotal)
{
    Q_ASSERT(sender());
    Q_ASSERT(qobject_cast<QNetworkReply *>(sender()));
    QNetworkReply *reply = static_cast<QNetworkReply *>(sender());
    l->networkReplyProgress(reply, bytesReceived, bytesTotal);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypeloadernetworkreplyproxy.cpp, line 16, as _ZN31QQmlTypeLoaderNetworkReplyProxy8finishedEv
inline void QQmlTypeLoaderNetworkReplyProxy::finished()
{
    Q_ASSERT(sender());
    Q_ASSERT(qobject_cast<QNetworkReply *>(sender()));
    QNetworkReply *reply = static_cast<QNetworkReply *>(sender());
    l->networkReplyFinished(reply);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypeloadernetworkreplyproxy.cpp, line 10, as _ZN31QQmlTypeLoaderNetworkReplyProxyC1EP14QQmlTypeLoaderP7QObject
inline QQmlTypeLoaderNetworkReplyProxy::QQmlTypeLoaderNetworkReplyProxy(
        QQmlTypeLoader *l, QObject *parent)
    : QObject(parent), l(l)
{
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQmlTypeLoaderNetworkReplyProxy::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QQmlTypeLoaderNetworkReplyProxy10metaObjectEv(
    const QQmlTypeLoaderNetworkReplyProxy *self) {
  return self->metaObject();
}

//  void *QQmlTypeLoaderNetworkReplyProxy::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN31QQmlTypeLoaderNetworkReplyProxy11qt_metacastEPKc(
    QQmlTypeLoaderNetworkReplyProxy *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlTypeLoaderNetworkReplyProxy::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN31QQmlTypeLoaderNetworkReplyProxy11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlTypeLoaderNetworkReplyProxy *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlTypeLoaderNetworkReplyProxy::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN31QQmlTypeLoaderNetworkReplyProxy2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlTypeLoaderNetworkReplyProxy::tr(s, c, n));
}

//  QQmlTypeLoaderNetworkReplyProxy::QQmlTypeLoaderNetworkReplyProxy(QQmlType
//      Loader *l, QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlTypeLoaderNetworkReplyProxy *ritual_ZN31QQmlTypeLoaderNetworkReplyProxyC1EP14QQmlTypeLoaderP7QObject(
    QQmlTypeLoader *l,
    QObject *parent) {
  return new QQmlTypeLoaderNetworkReplyProxy(l, parent);
}

//  void QQmlTypeLoaderNetworkReplyProxy::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlTypeLoaderNetworkReplyProxy8finishedEv(
    QQmlTypeLoaderNetworkReplyProxy *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQmlTypeLoaderNetworkReplyProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "finished()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "finished()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQmlTypeLoaderNetworkReplyProxy::downloadProgress(qint64 a0, qint64
//      a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlTypeLoaderNetworkReplyProxy16downloadProgressExx(
    QQmlTypeLoaderNetworkReplyProxy *self,
    qint64 a0,
    qint64 a1) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQmlTypeLoaderNetworkReplyProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "downloadProgress(qint64,qint64)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "downloadProgress(qint64,qint64)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&a0)),
      const_cast<void *>(static_cast<const void *>(&a1)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQmlTypeLoaderNetworkReplyProxy::manualFinished(QNetworkReply *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlTypeLoaderNetworkReplyProxy14manualFinishedEP13QNetworkReply(
    QQmlTypeLoaderNetworkReplyProxy *self,
    QNetworkReply *a0) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQmlTypeLoaderNetworkReplyProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "manualFinished(QNetworkReply *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "manualFinished(QNetworkReply *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&a0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#endif  // QT_CONFIG(qml_network)
#endif  // QT_CONFIG(qml_network)
