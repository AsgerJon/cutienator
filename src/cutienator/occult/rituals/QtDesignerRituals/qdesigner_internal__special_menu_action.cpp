//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_menubar_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'qdesigner_internal::SpecialMenuAction' is pasted in, cut from what the
//  moc of Qt 6.12.0 writes for its header: Qt's library keeps it to itself;
//  added are 2 rituals that lean on what moc writes for a class of the part
//  Qt keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_menubar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtDesigner/private/qdesigner_menubar_p.h>
#include <QtDesigner/private/qdesigner_menu_p.h>
#include <QtDesigner/private/qdesigner_command_p.h>
#include <QtDesigner/private/actionrepository_p.h>
#include <QtDesigner/private/actionprovider_p.h>
#include <QtDesigner/private/actioneditor_p.h>
#include <QtDesigner/private/menuactionlineedit_p.h>
#include <QtDesigner/private/qdesigner_utils_p.h>
#include <QtDesigner/private/promotiontaskmenu_p.h>
#include <QtDesigner/private/qdesigner_objectinspector_p.h>
#include <QtDesigner/abstractformwindow.h>
#include <QtDesigner/abstractformeditor.h>
#include <QtDesigner/abstractwidgetfactory.h>
#include <QtDesigner/qextensionmanager.h>
#include <QtCore/qmimedata.h>
#include <QtCore/qdebug.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qdrag.h>
#include <QtWidgets/qlineedit.h>
#include <QtGui/qpainter.h>
#include <QtGui/qevent.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only WITH Qt-GPL-exception-1.0
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from QtDesigner__qdesigner_internal_SpecialMenuAction.cpp, line 1, as moc:qdesigner_internal::SpecialMenuAction
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN18qdesigner_internal17SpecialMenuActionE_t {};
} // unnamed namespace

template <> constexpr inline auto qdesigner_internal::SpecialMenuAction::qt_create_metaobjectdata<qt_meta_tag_ZN18qdesigner_internal17SpecialMenuActionE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "qdesigner_internal::SpecialMenuAction"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<SpecialMenuAction, qt_meta_tag_ZN18qdesigner_internal17SpecialMenuActionE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject qdesigner_internal::SpecialMenuAction::staticMetaObject = { {
    QMetaObject::SuperData::link<QAction::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18qdesigner_internal17SpecialMenuActionE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18qdesigner_internal17SpecialMenuActionE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN18qdesigner_internal17SpecialMenuActionE_t>.metaTypes,
    nullptr
} };

void qdesigner_internal::SpecialMenuAction::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<SpecialMenuAction *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *qdesigner_internal::SpecialMenuAction::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *qdesigner_internal::SpecialMenuAction::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18qdesigner_internal17SpecialMenuActionE_t>.strings))
        return static_cast<void*>(this);
    return QAction::qt_metacast(_clname);
}

int qdesigner_internal::SpecialMenuAction::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QAction::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qttools/src/designer/src/lib/shared/qdesigner_menubar.cpp, line 47, as _ZN18qdesigner_internal17SpecialMenuActionD0Ev
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline SpecialMenuAction::~SpecialMenuAction() = default;
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_menubar.cpp, line 42, as _ZN18qdesigner_internal17SpecialMenuActionC1EP7QObject
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline SpecialMenuAction::SpecialMenuAction(QObject *parent)
    : QAction(parent)
{
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  A qdesigner_internal::SpecialMenuAction that Python can take functions over in. Every qdesigner_internal::SpecialMenuAction
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(action)
typedef bool (*Cuteqdesigner_internal_SpecialMenuActionCall0)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(action)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_SpecialMenuActionCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_SpecialMenuActionCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_SpecialMenuActionCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_SpecialMenuActionCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_SpecialMenuActionCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_SpecialMenuActionCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class Cuteqdesigner_internal_SpecialMenuAction : public qdesigner_internal::SpecialMenuAction {
public:
  using qdesigner_internal::SpecialMenuAction::SpecialMenuAction;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(action)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(action)
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
#if QT_CONFIG(action)
  //  bool QAction::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_SpecialMenuActionCall0 call = reinterpret_cast<Cuteqdesigner_internal_SpecialMenuActionCall0>(taken[0]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QAction::event(a0);
  }
#endif  // QT_CONFIG(action)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_SpecialMenuActionCall1 call = reinterpret_cast<Cuteqdesigner_internal_SpecialMenuActionCall1>(taken[1]);
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
      Cuteqdesigner_internal_SpecialMenuActionCall2 call = reinterpret_cast<Cuteqdesigner_internal_SpecialMenuActionCall2>(taken[2]);
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
      Cuteqdesigner_internal_SpecialMenuActionCall3 call = reinterpret_cast<Cuteqdesigner_internal_SpecialMenuActionCall3>(taken[3]);
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
      Cuteqdesigner_internal_SpecialMenuActionCall4 call = reinterpret_cast<Cuteqdesigner_internal_SpecialMenuActionCall4>(taken[4]);
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
      Cuteqdesigner_internal_SpecialMenuActionCall5 call = reinterpret_cast<Cuteqdesigner_internal_SpecialMenuActionCall5>(taken[5]);
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
      Cuteqdesigner_internal_SpecialMenuActionCall6 call = reinterpret_cast<Cuteqdesigner_internal_SpecialMenuActionCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *qdesigner_internal::SpecialMenuAction::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal17SpecialMenuAction10metaObjectEv(
    const qdesigner_internal::SpecialMenuAction *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::SpecialMenuAction::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal17SpecialMenuAction11qt_metacastEPKc(
    qdesigner_internal::SpecialMenuAction *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::SpecialMenuAction::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal17SpecialMenuAction11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::SpecialMenuAction *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString qdesigner_internal::SpecialMenuAction::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal17SpecialMenuAction2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::SpecialMenuAction::tr(s, c, n));
}

//  qdesigner_internal::SpecialMenuAction::SpecialMenuAction(QObject *parent)
extern "C" Q_DECL_EXPORT
qdesigner_internal::SpecialMenuAction *ritual_ZN18qdesigner_internal17SpecialMenuActionC1EP7QObject(
    QObject *parent) {
  return new Cuteqdesigner_internal_SpecialMenuAction(parent);
}

//  qdesigner_internal::SpecialMenuAction::~SpecialMenuAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal17SpecialMenuActionD1Ev(
    qdesigner_internal::SpecialMenuAction *self) {
  delete self;
}

//  a Python function taken by a Cuteqdesigner_internal_SpecialMenuAction,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_SpecialMenuAction(
    qdesigner_internal::SpecialMenuAction *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_SpecialMenuAction *>(self)->take(key, call);
}
