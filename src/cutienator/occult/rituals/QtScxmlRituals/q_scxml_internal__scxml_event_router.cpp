//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlstatemachine_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QScxmlInternal::ScxmlEventRouter' is pasted in, cut from what the moc of
//  Qt 6.12.0 writes for its header: Qt's library keeps it to itself; added
//  are 6 rituals that lean on what moc writes for a class of the part Qt
//  keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlstatemachine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qobjectdefs.h>
#include <QtScxml/qscxmlevent.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtScxml/private/qscxmlstatemachine_p.h>
#include <QtScxml/private/qscxmlexecutablecontent_p.h>
#include <QtScxml/private/qscxmlevent_p.h>
#include <QtScxml/qscxmlinvokableservice.h>
#include <QtScxml/private/qscxmldatamodel_p.h>
#include <QtCore/qfile.h>
#include <QtCore/qhash.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qstring.h>
#include <QtCore/qtimer.h>
#include <QtCore/qthread.h>
#include <functional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtscxml/src/scxml/qscxmlstatemachine.cpp, line 253, as local:qscxmlstatemachine.cpp:nextSegment
namespace QScxmlInternal {
static QString nextSegment(const QStringList &segments)
{
    if (segments.isEmpty())
        return QString();

    const QString &segment = segments.first();
    return segment == QLatin1String("*") ? QString() : segment;
}
}  // namespace QScxmlInternal

//  from QtScxml__QScxmlInternal_ScxmlEventRouter.cpp, line 1, as moc:QScxmlInternal::ScxmlEventRouter
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN14QScxmlInternal16ScxmlEventRouterE_t {};
} // unnamed namespace

template <> constexpr inline auto QScxmlInternal::ScxmlEventRouter::qt_create_metaobjectdata<qt_meta_tag_ZN14QScxmlInternal16ScxmlEventRouterE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QScxmlInternal::ScxmlEventRouter",
        "eventOccurred",
        "",
        "QScxmlEvent",
        "event"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'eventOccurred'
        QtMocHelpers::SignalData<void(const QScxmlEvent &)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 3, 4 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<ScxmlEventRouter, qt_meta_tag_ZN14QScxmlInternal16ScxmlEventRouterE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QScxmlInternal::ScxmlEventRouter::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN14QScxmlInternal16ScxmlEventRouterE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN14QScxmlInternal16ScxmlEventRouterE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN14QScxmlInternal16ScxmlEventRouterE_t>.metaTypes,
    nullptr
} };

void QScxmlInternal::ScxmlEventRouter::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<ScxmlEventRouter *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->eventOccurred((*reinterpret_cast<std::add_pointer_t<QScxmlEvent>>(_a[1]))); break;
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
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QScxmlEvent >(); break;
            }
            break;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (ScxmlEventRouter::*)(const QScxmlEvent & )>(_a, &ScxmlEventRouter::eventOccurred, 0))
            return;
    }
}

const QMetaObject *QScxmlInternal::ScxmlEventRouter::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QScxmlInternal::ScxmlEventRouter::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN14QScxmlInternal16ScxmlEventRouterE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QScxmlInternal::ScxmlEventRouter::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    return _id;
}

// SIGNAL 0
void QScxmlInternal::ScxmlEventRouter::eventOccurred(const QScxmlEvent & _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1);
}
QT_WARNING_POP

//  from ../qtscxml/src/scxml/qscxmlstatemachine.cpp, line 270, as _ZN14QScxmlInternal16ScxmlEventRouter16disconnectNotifyERK11QMetaMethod
namespace QScxmlInternal {
inline void ScxmlEventRouter::disconnectNotify(const QMetaMethod &signal)
{
    Q_UNUSED(signal);

    // Defer the actual work, as this may be called from a destructor, or the signal may not
    // actually be disconnected, yet.
    QTimer::singleShot(0, this, [this] {
        if (!children.isEmpty() || receivers(SIGNAL(eventOccurred(QScxmlEvent))) > 0)
            return;

        ScxmlEventRouter *parentRouter = qobject_cast<ScxmlEventRouter *>(parent());
        if (!parentRouter) // root node
            return;

        QHash<QString, ScxmlEventRouter *>::Iterator it = parentRouter->children.begin(),
                end = parentRouter->children.end();
        for (; it != end; ++it) {
            if (it.value() == this) {
                parentRouter->children.erase(it);
                parentRouter->disconnectNotify(QMetaMethod());
                break;
            }
        }

        deleteLater(); // The parent might delete itself, triggering QObject delete cascades.
    });
}
}  // namespace QScxmlInternal

//  from ../qtscxml/src/scxml/qscxmlstatemachine.cpp, line 298, as _ZN14QScxmlInternal16ScxmlEventRouter14connectToEventERK5QListI7QStringEPK7QObjectPKcN2Qt14ConnectionTypeE
namespace QScxmlInternal {
inline QMetaObject::Connection ScxmlEventRouter::connectToEvent(const QStringList &segments,
                                                         const QObject *receiver,
                                                         const char *method,
                                                         Qt::ConnectionType type)
{
    QString segment = nextSegment(segments);
    return segment.isEmpty() ?
                connect(this, SIGNAL(eventOccurred(QScxmlEvent)), receiver, method, type) :
                child(segment)->connectToEvent(segments.mid(1), receiver, method, type);
}
}  // namespace QScxmlInternal

//  from ../qtscxml/src/scxml/qscxmlstatemachine.cpp, line 243, as _ZN14QScxmlInternal16ScxmlEventRouter5routeERK5QListI7QStringEP11QScxmlEvent
namespace QScxmlInternal {
inline void ScxmlEventRouter::route(const QStringList &segments, QScxmlEvent *event)
{
    emit eventOccurred(*event);
    if (!segments.isEmpty()) {
        auto it = children.find(segments.first());
        if (it != children.end())
            it.value()->route(segments.mid(1), event);
    }
}
}  // namespace QScxmlInternal

//  from ../qtscxml/src/scxml/qscxmlstatemachine.cpp, line 262, as _ZN14QScxmlInternal16ScxmlEventRouter5childERK7QString
namespace QScxmlInternal {
inline ScxmlEventRouter *ScxmlEventRouter::child(const QString &segment)
{
    ScxmlEventRouter *&child = children[segment];
    if (child == nullptr)
        child = new ScxmlEventRouter(this);
    return child;
}
}  // namespace QScxmlInternal
//  -----------------------------------------------------------------------

//  const QMetaObject *QScxmlInternal::ScxmlEventRouter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QScxmlInternal16ScxmlEventRouter10metaObjectEv(
    const QScxmlInternal::ScxmlEventRouter *self) {
  return self->metaObject();
}

//  void *QScxmlInternal::ScxmlEventRouter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QScxmlInternal16ScxmlEventRouter11qt_metacastEPKc(
    QScxmlInternal::ScxmlEventRouter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QScxmlInternal::ScxmlEventRouter::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QScxmlInternal16ScxmlEventRouter11qt_metacallEN11QMetaObject4CallEiPPv(
    QScxmlInternal::ScxmlEventRouter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QScxmlInternal::ScxmlEventRouter::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QScxmlInternal16ScxmlEventRouter2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScxmlInternal::ScxmlEventRouter::tr(s, c, n));
}

//  QScxmlInternal::ScxmlEventRouter::ScxmlEventRouter(QObject *parent)
extern "C" Q_DECL_EXPORT
QScxmlInternal::ScxmlEventRouter *ritual_ZN14QScxmlInternal16ScxmlEventRouterC1EP7QObject(
    QObject *parent) {
  return new QScxmlInternal::ScxmlEventRouter(parent);
}

//  QMetaObject::Connection
//      QScxmlInternal::ScxmlEventRouter::connectToEvent(const QStringList
//      &segments, const QObject *receiver, const char *method,
//      Qt::ConnectionType type)
extern "C" Q_DECL_EXPORT
QMetaObject::Connection *ritual_ZN14QScxmlInternal16ScxmlEventRouter14connectToEventERK5QListI7QStringEPK7QObjectPKcN2Qt14ConnectionTypeE(
    QScxmlInternal::ScxmlEventRouter *self,
    const QList<QString> *segments,
    const QObject *receiver,
    const char *method,
    Qt::ConnectionType type) {
  return new QMetaObject::Connection(
      self->connectToEvent(
          *segments,
          receiver,
          method,
          type));
}

//  void QScxmlInternal::ScxmlEventRouter::route(const QStringList &segments,
//      QScxmlEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScxmlInternal16ScxmlEventRouter5routeERK5QListI7QStringEP11QScxmlEvent(
    QScxmlInternal::ScxmlEventRouter *self,
    const QList<QString> *segments,
    QScxmlEvent *event) {
  self->route(*segments, event);
}

//  void QScxmlInternal::ScxmlEventRouter::eventOccurred(const QScxmlEvent
//      &event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScxmlInternal16ScxmlEventRouter13eventOccurredERK11QScxmlEvent(
    QScxmlInternal::ScxmlEventRouter *self,
    const QScxmlEvent *event) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QScxmlInternal::ScxmlEventRouter")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "eventOccurred(const QScxmlEvent &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "eventOccurred(const QScxmlEvent &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(event)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  ScxmlEventRouter *QScxmlInternal::ScxmlEventRouter::child(const QString
//      &segment)
extern "C" Q_DECL_EXPORT
QScxmlInternal::ScxmlEventRouter *ritual_ZN14QScxmlInternal16ScxmlEventRouter5childERK7QString(
    QScxmlInternal::ScxmlEventRouter *self,
    const QString *segment) {
  return self->child(*segment);
}

//  void QScxmlInternal::ScxmlEventRouter::disconnectNotify(const QMetaMethod
//      &signal)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScxmlInternal16ScxmlEventRouter16disconnectNotifyERK11QMetaMethod(
    QScxmlInternal::ScxmlEventRouter *self,
    const QMetaMethod *signal) {
  self->disconnectNotify(*signal);
}

//  void QScxmlInternal::ScxmlEventRouter::disconnectNotify(const QMetaMethod
//      &signal)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QScxmlInternal16ScxmlEventRouter16disconnectNotifyERK11QMetaMethod(
    QScxmlInternal::ScxmlEventRouter *self,
    const QMetaMethod *signal) {
  self->QScxmlInternal::ScxmlEventRouter::disconnectNotify(*signal);
}
