//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qremoteobjectregistrysource_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QRegistrySource' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectregistrysource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtRemoteObjects/qtremoteobjectglobal.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtCore/qloggingcategory.h>
#include <QtRemoteObjects/private/qremoteobjectregistrysource_p.h>
#include <QtCore/qdatastream.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtRemoteObjects__QRegistrySource.cpp, line 1, as moc:QRegistrySource
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN15QRegistrySourceE_t {};
} // unnamed namespace

template <> constexpr inline auto QRegistrySource::qt_create_metaobjectdata<qt_meta_tag_ZN15QRegistrySourceE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QRegistrySource",
        "RemoteObject Type",
        "Registry",
        "remoteObjectAdded",
        "",
        "QRemoteObjectSourceLocation",
        "entry",
        "remoteObjectRemoved",
        "addSource",
        "removeSource",
        "removeServer",
        "QUrl",
        "url",
        "sourceLocations",
        "QRemoteObjectSourceLocations"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'remoteObjectAdded'
        QtMocHelpers::SignalData<void(const QRemoteObjectSourceLocation &)>(3, 4, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 5, 6 },
        }}),
        // Signal 'remoteObjectRemoved'
        QtMocHelpers::SignalData<void(const QRemoteObjectSourceLocation &)>(7, 4, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 5, 6 },
        }}),
        // Slot 'addSource'
        QtMocHelpers::SlotData<void(const QRemoteObjectSourceLocation &)>(8, 4, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 5, 6 },
        }}),
        // Slot 'removeSource'
        QtMocHelpers::SlotData<void(const QRemoteObjectSourceLocation &)>(9, 4, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 5, 6 },
        }}),
        // Slot 'removeServer'
        QtMocHelpers::SlotData<void(const QUrl &)>(10, 4, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 11, 12 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'sourceLocations'
        QtMocHelpers::PropertyData<QRemoteObjectSourceLocations>(13, 0x80000000 | 14, QMC::DefaultPropertyFlags | QMC::EnumOrFlag),
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
    });
    return QtMocHelpers::metaObjectData<QRegistrySource, qt_meta_tag_ZN15QRegistrySourceE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QRegistrySource::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15QRegistrySourceE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15QRegistrySourceE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN15QRegistrySourceE_t>.metaTypes,
    nullptr
} };

void QRegistrySource::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QRegistrySource *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->remoteObjectAdded((*reinterpret_cast<std::add_pointer_t<QRemoteObjectSourceLocation>>(_a[1]))); break;
        case 1: _t->remoteObjectRemoved((*reinterpret_cast<std::add_pointer_t<QRemoteObjectSourceLocation>>(_a[1]))); break;
        case 2: _t->addSource((*reinterpret_cast<std::add_pointer_t<QRemoteObjectSourceLocation>>(_a[1]))); break;
        case 3: _t->removeSource((*reinterpret_cast<std::add_pointer_t<QRemoteObjectSourceLocation>>(_a[1]))); break;
        case 4: _t->removeServer((*reinterpret_cast<std::add_pointer_t<QUrl>>(_a[1]))); break;
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
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QRemoteObjectSourceLocation >(); break;
            }
            break;
        case 1:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QRemoteObjectSourceLocation >(); break;
            }
            break;
        case 2:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QRemoteObjectSourceLocation >(); break;
            }
            break;
        case 3:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QRemoteObjectSourceLocation >(); break;
            }
            break;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QRegistrySource::*)(const QRemoteObjectSourceLocation & )>(_a, &QRegistrySource::remoteObjectAdded, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QRegistrySource::*)(const QRemoteObjectSourceLocation & )>(_a, &QRegistrySource::remoteObjectRemoved, 1))
            return;
    }
    if (_c == QMetaObject::RegisterPropertyMetaType) {
        switch (_id) {
        default: *reinterpret_cast<int*>(_a[0]) = -1; break;
        case 0:
            *reinterpret_cast<int*>(_a[0]) = qRegisterMetaType< QRemoteObjectSourceLocations >(); break;
        }
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QRemoteObjectSourceLocations*>(_v) = _t->sourceLocations(); break;
        default: break;
        }
    }
}

const QMetaObject *QRegistrySource::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QRegistrySource::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15QRegistrySourceE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QRegistrySource::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    }
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    return _id;
}

// SIGNAL 0
void QRegistrySource::remoteObjectAdded(const QRemoteObjectSourceLocation & _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1);
}

// SIGNAL 1
void QRegistrySource::remoteObjectRemoved(const QRemoteObjectSourceLocation & _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 1, nullptr, _t1);
}
QT_WARNING_POP

//  from ../qtremoteobjects/src/remoteobjects/qtremoteobjectglobal.cpp, line 13, as _Z15QT_REMOTEOBJECTv
inline const QLoggingCategory &QT_REMOTEOBJECT()
{
    static const QLoggingCategory category("qt.remoteobjects", QtWarningMsg);
    return category;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectregistrysource.cpp, line 25, as _ZN15QRegistrySource12removeServerERK4QUrl
inline void QRegistrySource::removeServer(const QUrl &url)
{
    for (auto it = m_sourceLocations.begin(), end = m_sourceLocations.end(); it != end; /* erasing */) {
        if (it.value().hostUrl == url)
            it = m_sourceLocations.erase(it);
        else
            ++it;
    }
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectregistrysource.cpp, line 52, as _ZN15QRegistrySource12removeSourceERKSt4pairI7QString31QRemoteObjectSourceLocationInfoE
inline void QRegistrySource::removeSource(const QRemoteObjectSourceLocation &entry)
{
    if (m_sourceLocations.contains(entry.first) && m_sourceLocations[entry.first].hostUrl == entry.second.hostUrl) {
        m_sourceLocations.remove(entry.first);
        emit remoteObjectRemoved(entry);
    }
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectregistrysource.cpp, line 35, as _ZN15QRegistrySource9addSourceERKSt4pairI7QString31QRemoteObjectSourceLocationInfoE
inline void QRegistrySource::addSource(const QRemoteObjectSourceLocation &entry)
{
    qCDebug(QT_REMOTEOBJECT) << "An entry was added to the RegistrySource" << entry;
    if (m_sourceLocations.contains(entry.first)) {
        if (m_sourceLocations[entry.first].hostUrl == entry.second.hostUrl)
            qCWarning(QT_REMOTEOBJECT) << "Node warning: Ignoring Source" << entry.first
                                       << "as this Node already has a Source by that name.";
        else
            qCWarning(QT_REMOTEOBJECT) << "Node warning: Ignoring Source" << entry.first
                                       << "as another source (" << m_sourceLocations[entry.first]
                                       << ") has already registered that name.";
        return;
    }
    m_sourceLocations[entry.first] = entry.second;
    emit remoteObjectAdded(entry);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectregistrysource.cpp, line 15, as _ZN15QRegistrySourceD0Ev
inline QRegistrySource::~QRegistrySource()
{
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectregistrysource.cpp, line 10, as _ZN15QRegistrySourceC1EP7QObject
inline QRegistrySource::QRegistrySource(QObject *parent)
    : QObject(parent)
{
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectregistrysource.cpp, line 19, as _ZNK15QRegistrySource15sourceLocationsEv
inline QRemoteObjectSourceLocations QRegistrySource::sourceLocations() const
{
    qCDebug(QT_REMOTEOBJECT) << "sourceLocations property requested on RegistrySource" << m_sourceLocations;
    return m_sourceLocations;
}
//  -----------------------------------------------------------------------

//  A QRegistrySource that Python can take functions over in. Every QRegistrySource
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRegistrySourceCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRegistrySourceCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRegistrySourceCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRegistrySourceCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRegistrySourceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRegistrySourceCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRegistrySourceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRegistrySource : public QRegistrySource {
public:
  using QRegistrySource::QRegistrySource;
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
      CuteQRegistrySourceCall0 call = reinterpret_cast<CuteQRegistrySourceCall0>(taken[0]);
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
      CuteQRegistrySourceCall1 call = reinterpret_cast<CuteQRegistrySourceCall1>(taken[1]);
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
      CuteQRegistrySourceCall2 call = reinterpret_cast<CuteQRegistrySourceCall2>(taken[2]);
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
      CuteQRegistrySourceCall3 call = reinterpret_cast<CuteQRegistrySourceCall3>(taken[3]);
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
      CuteQRegistrySourceCall4 call = reinterpret_cast<CuteQRegistrySourceCall4>(taken[4]);
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
      CuteQRegistrySourceCall5 call = reinterpret_cast<CuteQRegistrySourceCall5>(taken[5]);
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
      CuteQRegistrySourceCall6 call = reinterpret_cast<CuteQRegistrySourceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QRegistrySource::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QRegistrySource10metaObjectEv(
    const QRegistrySource *self) {
  return self->metaObject();
}

//  void *QRegistrySource::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QRegistrySource11qt_metacastEPKc(
    QRegistrySource *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QRegistrySource::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QRegistrySource11qt_metacallEN11QMetaObject4CallEiPPv(
    QRegistrySource *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QRegistrySource::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QRegistrySource2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRegistrySource::tr(s, c, n));
}

//  QRegistrySource::QRegistrySource(QObject *parent)
extern "C" Q_DECL_EXPORT
QRegistrySource *ritual_ZN15QRegistrySourceC1EP7QObject(QObject *parent) {
  return new CuteQRegistrySource(parent);
}

//  QRegistrySource::~QRegistrySource()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRegistrySourceD1Ev(QRegistrySource *self) {
  delete self;
}

//  QRemoteObjectSourceLocations QRegistrySource::sourceLocations() const
extern "C" Q_DECL_EXPORT
QHash<QString, QRemoteObjectSourceLocationInfo> *ritual_ZNK15QRegistrySource15sourceLocationsEv(
    const QRegistrySource *self) {
  return new QHash<QString, QRemoteObjectSourceLocationInfo>(
      self->sourceLocations());
}

//  void QRegistrySource::remoteObjectAdded(const QRemoteObjectSourceLocation
//      &entry)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRegistrySource17remoteObjectAddedERKSt4pairI7QString31QRemoteObjectSourceLocationInfoE(
    QRegistrySource *self,
    const QRemoteObjectSourceLocation *entry) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QRegistrySource")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "remoteObjectAdded(const QRemoteObjectSourceLocation &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "remoteObjectAdded(const QRemoteObjectSourceLocation &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(entry)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QRegistrySource::remoteObjectRemoved(const
//      QRemoteObjectSourceLocation &entry)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRegistrySource19remoteObjectRemovedERKSt4pairI7QString31QRemoteObjectSourceLocationInfoE(
    QRegistrySource *self,
    const QRemoteObjectSourceLocation *entry) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QRegistrySource")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "remoteObjectRemoved(const QRemoteObjectSourceLocation &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "remoteObjectRemoved(const QRemoteObjectSourceLocation &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(entry)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QRegistrySource::addSource(const QRemoteObjectSourceLocation &entry)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRegistrySource9addSourceERKSt4pairI7QString31QRemoteObjectSourceLocationInfoE(
    QRegistrySource *self,
    const QRemoteObjectSourceLocation *entry) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QRegistrySource")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "addSource(const QRemoteObjectSourceLocation &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "addSource(const QRemoteObjectSourceLocation &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(entry)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QRegistrySource::removeSource(const QRemoteObjectSourceLocation
//      &entry)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRegistrySource12removeSourceERKSt4pairI7QString31QRemoteObjectSourceLocationInfoE(
    QRegistrySource *self,
    const QRemoteObjectSourceLocation *entry) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QRegistrySource")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "removeSource(const QRemoteObjectSourceLocation &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "removeSource(const QRemoteObjectSourceLocation &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(entry)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QRegistrySource::removeServer(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRegistrySource12removeServerERK4QUrl(
    QRegistrySource *self,
    const QUrl *url) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QRegistrySource")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "removeServer(const QUrl &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "removeServer(const QUrl &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(url)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQRegistrySource, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRegistrySource(
    QRegistrySource *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRegistrySource *>(self)->take(key, call);
}
