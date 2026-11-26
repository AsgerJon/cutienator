//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DLogic/6.12.0/Qt3DLogic/private/executor_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'Qt3DLogic::Logic::Executor' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  2 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DLogic/Qt3DLogic>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DLogic/6.12.0/Qt3DLogic/private/executor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <Qt3DLogic/private/executor_p.h>
#include <Qt3DLogic/qframeaction.h>
#include <Qt3DCore/qnode.h>
#include <QtCore/qsemaphore.h>
#include <Qt3DCore/private/qscene_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from Qt3DLogic__Qt3DLogic_Logic_Executor.cpp, line 1, as moc:Qt3DLogic::Logic::Executor
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN9Qt3DLogic5Logic8ExecutorE_t {};
} // unnamed namespace

template <> constexpr inline auto Qt3DLogic::Logic::Executor::qt_create_metaobjectdata<qt_meta_tag_ZN9Qt3DLogic5Logic8ExecutorE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "Qt3DLogic::Logic::Executor",
        "processLogicFrameUpdates",
        "",
        "QList<Qt3DCore::QNodeId>",
        "nodeIds",
        "dt"
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'processLogicFrameUpdates'
        QtMocHelpers::SlotData<void(const QList<Qt3DCore::QNodeId> &, float)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 3, 4 }, { QMetaType::Float, 5 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<Executor, qt_meta_tag_ZN9Qt3DLogic5Logic8ExecutorE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject Qt3DLogic::Logic::Executor::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN9Qt3DLogic5Logic8ExecutorE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN9Qt3DLogic5Logic8ExecutorE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN9Qt3DLogic5Logic8ExecutorE_t>.metaTypes,
    nullptr
} };

void Qt3DLogic::Logic::Executor::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<Executor *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->processLogicFrameUpdates((*reinterpret_cast<std::add_pointer_t<QList<Qt3DCore::QNodeId>>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<float>>(_a[2]))); break;
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
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QList<Qt3DCore::QNodeId> >(); break;
            }
            break;
        }
    }
}

const QMetaObject *Qt3DLogic::Logic::Executor::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *Qt3DLogic::Logic::Executor::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN9Qt3DLogic5Logic8ExecutorE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int Qt3DLogic::Logic::Executor::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
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
QT_WARNING_POP

//  from ../qt3d/src/logic/executor.cpp, line 29, as _ZN9Qt3DLogic5Logic8Executor24processLogicFrameUpdatesERK5QListIN8Qt3DCore7QNodeIdEEf
namespace Qt3DLogic::Logic {
using namespace Qt3DCore;
inline void Executor::processLogicFrameUpdates(const QList<QNodeId> &nodeIds, float dt)
{
    if (!m_scene || nodeIds.isEmpty())
        return;

    const QList<QNode *> nodes = m_scene->lookupNodes(nodeIds);
    for (QNode *node : nodes) {
        QFrameAction *frameAction = qobject_cast<QFrameAction *>(node);
        if (frameAction && frameAction->isEnabled())
            frameAction->onTriggered(dt);
    }
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/executor.cpp, line 20, as _ZN9Qt3DLogic5Logic8ExecutorC1EP7QObject
namespace Qt3DLogic::Logic {
using namespace Qt3DCore;
inline Executor::Executor(QObject *parent)
    : QObject(parent)
    , m_scene(nullptr)
{
}
}  // namespace Qt3DLogic::Logic
//  -----------------------------------------------------------------------

//  const QMetaObject *Qt3DLogic::Logic::Executor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DLogic5Logic8Executor10metaObjectEv(
    const Qt3DLogic::Logic::Executor *self) {
  return self->metaObject();
}

//  void *Qt3DLogic::Logic::Executor::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DLogic5Logic8Executor11qt_metacastEPKc(
    Qt3DLogic::Logic::Executor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DLogic::Logic::Executor::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DLogic5Logic8Executor11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DLogic::Logic::Executor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DLogic::Logic::Executor::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DLogic5Logic8Executor2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DLogic::Logic::Executor::tr(s, c, n));
}

//  Qt3DLogic::Logic::Executor::Executor(QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DLogic::Logic::Executor *ritual_ZN9Qt3DLogic5Logic8ExecutorC1EP7QObject(
    QObject *parent) {
  return new Qt3DLogic::Logic::Executor(parent);
}

//  void Qt3DLogic::Logic::Executor::setScene(Qt3DCore::QScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DLogic5Logic8Executor8setSceneEPN8Qt3DCore6QSceneE(
    Qt3DLogic::Logic::Executor *self,
    Qt3DCore::QScene *scene) {
  self->setScene(scene);
}

//  void Qt3DLogic::Logic::Executor::processLogicFrameUpdates(const
//      QList<Qt3DCore::QNodeId> &nodeIds, float dt)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DLogic5Logic8Executor24processLogicFrameUpdatesERK5QListIN8Qt3DCore7QNodeIdEEf(
    Qt3DLogic::Logic::Executor *self,
    const QList<Qt3DCore::QNodeId> *nodeIds,
    float dt) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DLogic::Logic::Executor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "processLogicFrameUpdates(const QList<Qt3DCore::QNodeId> &,float)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "processLogicFrameUpdates(const QList<Qt3DCore::QNodeId> &,float)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(nodeIds)),
      const_cast<void *>(static_cast<const void *>(&dt)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
