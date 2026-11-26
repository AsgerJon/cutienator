//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qnode_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'Qt3DCore::NodePostConstructorInit' is pasted in, cut from what the moc
//  of Qt 6.12.0 writes for its header: Qt's library keeps it to itself;
//  added are 2 rituals that lean on what moc writes for a class of the part
//  Qt keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <Qt3DCore/qnode.h>
#include <Qt3DCore/private/qnode_p.h>
#include <Qt3DCore/private/qscene_p.h>
#include <Qt3DCore/QComponent>
#include <Qt3DCore/qaspectengine.h>
#include <Qt3DCore/qentity.h>
#include <QtCore/QChildEvent>
#include <QtCore/QEvent>
#include <QtCore/QMetaObject>
#include <QtCore/QMetaProperty>
#include <QtCore/QThread>
#include <Qt3DCore/private/corelogging_p.h>
#include <Qt3DCore/private/qdestructionidandtypecollector_p.h>
#include <Qt3DCore/private/qnodevisitor_p.h>
#include <Qt3DCore/private/qscene_p.h>
#include <Qt3DCore/private/qaspectengine_p.h>
#include <Qt3DCore/private/qaspectmanager_p.h>
#include <QtCore/private/qmetaobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from Qt3DCore__Qt3DCore_NodePostConstructorInit.cpp, line 1, as moc:Qt3DCore::NodePostConstructorInit
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN8Qt3DCore23NodePostConstructorInitE_t {};
} // unnamed namespace

template <> constexpr inline auto Qt3DCore::NodePostConstructorInit::qt_create_metaobjectdata<qt_meta_tag_ZN8Qt3DCore23NodePostConstructorInitE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "Qt3DCore::NodePostConstructorInit",
        "processNodes",
        ""
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'processNodes'
        QtMocHelpers::SlotData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<NodePostConstructorInit, qt_meta_tag_ZN8Qt3DCore23NodePostConstructorInitE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject Qt3DCore::NodePostConstructorInit::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN8Qt3DCore23NodePostConstructorInitE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN8Qt3DCore23NodePostConstructorInitE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN8Qt3DCore23NodePostConstructorInitE_t>.metaTypes,
    nullptr
} };

void Qt3DCore::NodePostConstructorInit::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<NodePostConstructorInit *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->processNodes(); break;
        default: ;
        }
    }
    (void)_a;
}

const QMetaObject *Qt3DCore::NodePostConstructorInit::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *Qt3DCore::NodePostConstructorInit::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN8Qt3DCore23NodePostConstructorInitE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int Qt3DCore::NodePostConstructorInit::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
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
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 1;
    }
    return _id;
}
QT_WARNING_POP

//  from ../qt3d/src/core/nodes/qnode.cpp, line 887, as _ZN8Qt3DCore23NodePostConstructorInit12processNodesEv
namespace Qt3DCore {
inline void NodePostConstructorInit::processNodes()
{
    Q_ASSERT(thread() == QThread::currentThread());
    m_requestedProcessing = false;
    while (!m_nodesToConstruct.empty()) {
        auto node = m_nodesToConstruct.takeFirst();
        node->_q_postConstructorInit();
    }
}
}  // namespace Qt3DCore

//  from ../qt3d/src/core/nodes/qnode.cpp, line 838, as _ZN8Qt3DCore23NodePostConstructorInitD0Ev
namespace Qt3DCore {
inline NodePostConstructorInit::~NodePostConstructorInit() {}
}  // namespace Qt3DCore

//  from ../qt3d/src/core/nodes/qnode.cpp, line 832, as _ZN8Qt3DCore23NodePostConstructorInitC1EP7QObject
namespace Qt3DCore {
inline NodePostConstructorInit::NodePostConstructorInit(QObject *parent)
    : QObject(parent)
    , m_requestedProcessing(false)
{
}
}  // namespace Qt3DCore

//  from ../qt3d/src/core/nodes/qnode.cpp, line 875, as _ZN8Qt3DCore23NodePostConstructorInit10removeNodeEPNS_5QNodeE
namespace Qt3DCore {
inline void NodePostConstructorInit::removeNode(QNode *node)
{
    Q_ASSERT(node);
    m_nodesToConstruct.removeAll(QNodePrivate::get(node));
}
}  // namespace Qt3DCore

//  from ../qt3d/src/core/nodes/qnode.cpp, line 850, as _ZN8Qt3DCore23NodePostConstructorInit7addNodeEPNS_5QNodeE
namespace Qt3DCore {
inline void NodePostConstructorInit::addNode(QNode *node)
{
    Q_ASSERT(node);
    QNode *nextNode = node;
    while (nextNode != nullptr && !m_nodesToConstruct.contains(QNodePrivate::get(nextNode)))
        nextNode = nextNode->parentNode();

    // An ancestor in the m_nodesToConstruct may already have been created (m_hasBackendNode)
    // at this point (e.g. when a QComponent calls _q_ensureBackendNodeCreated()),
    // that's why we also queue a creation request in this case.
    if (!nextNode || QNodePrivate::get(nextNode)->m_hasBackendNode) {
        m_nodesToConstruct.append(QNodePrivate::get(node));
        if (!m_requestedProcessing){
            QMetaObject::invokeMethod(this, "processNodes", Qt::QueuedConnection);
            m_requestedProcessing = true;
        }
    }
}
}  // namespace Qt3DCore
//  -----------------------------------------------------------------------

//  A Qt3DCore::NodePostConstructorInit that Python can take functions over in. Every Qt3DCore::NodePostConstructorInit
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_NodePostConstructorInitCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_NodePostConstructorInitCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_NodePostConstructorInitCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_NodePostConstructorInitCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_NodePostConstructorInitCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_NodePostConstructorInitCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_NodePostConstructorInitCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_NodePostConstructorInit : public Qt3DCore::NodePostConstructorInit {
public:
  using Qt3DCore::NodePostConstructorInit::NodePostConstructorInit;
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
      CuteQt3DCore_NodePostConstructorInitCall0 call = reinterpret_cast<CuteQt3DCore_NodePostConstructorInitCall0>(taken[0]);
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
      CuteQt3DCore_NodePostConstructorInitCall1 call = reinterpret_cast<CuteQt3DCore_NodePostConstructorInitCall1>(taken[1]);
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
      CuteQt3DCore_NodePostConstructorInitCall2 call = reinterpret_cast<CuteQt3DCore_NodePostConstructorInitCall2>(taken[2]);
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
      CuteQt3DCore_NodePostConstructorInitCall3 call = reinterpret_cast<CuteQt3DCore_NodePostConstructorInitCall3>(taken[3]);
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
      CuteQt3DCore_NodePostConstructorInitCall4 call = reinterpret_cast<CuteQt3DCore_NodePostConstructorInitCall4>(taken[4]);
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
      CuteQt3DCore_NodePostConstructorInitCall5 call = reinterpret_cast<CuteQt3DCore_NodePostConstructorInitCall5>(taken[5]);
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
      CuteQt3DCore_NodePostConstructorInitCall6 call = reinterpret_cast<CuteQt3DCore_NodePostConstructorInitCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::NodePostConstructorInit::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore23NodePostConstructorInit10metaObjectEv(
    const Qt3DCore::NodePostConstructorInit *self) {
  return self->metaObject();
}

//  void *Qt3DCore::NodePostConstructorInit::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore23NodePostConstructorInit11qt_metacastEPKc(
    Qt3DCore::NodePostConstructorInit *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::NodePostConstructorInit::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore23NodePostConstructorInit11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::NodePostConstructorInit *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::NodePostConstructorInit::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore23NodePostConstructorInit2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::NodePostConstructorInit::tr(s, c, n));
}

//  Qt3DCore::NodePostConstructorInit::NodePostConstructorInit(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::NodePostConstructorInit *ritual_ZN8Qt3DCore23NodePostConstructorInitC1EP7QObject(
    QObject *parent) {
  return new CuteQt3DCore_NodePostConstructorInit(parent);
}

//  Qt3DCore::NodePostConstructorInit::~NodePostConstructorInit()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore23NodePostConstructorInitD1Ev(
    Qt3DCore::NodePostConstructorInit *self) {
  delete self;
}

//  void Qt3DCore::NodePostConstructorInit::removeNode(QNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore23NodePostConstructorInit10removeNodeEPNS_5QNodeE(
    Qt3DCore::NodePostConstructorInit *self,
    Qt3DCore::QNode *node) {
  self->removeNode(node);
}

//  void Qt3DCore::NodePostConstructorInit::addNode(QNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore23NodePostConstructorInit7addNodeEPNS_5QNodeE(
    Qt3DCore::NodePostConstructorInit *self,
    Qt3DCore::QNode *node) {
  self->addNode(node);
}

//  void Qt3DCore::NodePostConstructorInit::processNodes()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore23NodePostConstructorInit12processNodesEv(
    Qt3DCore::NodePostConstructorInit *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DCore::NodePostConstructorInit")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "processNodes()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "processNodes()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQt3DCore_NodePostConstructorInit, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_NodePostConstructorInit(
    Qt3DCore::NodePostConstructorInit *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_NodePostConstructorInit *>(self)->take(key, call);
}
