//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/menuactionlineedit_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'qdesigner_internal::MenuActionLineEdit' is pasted in, cut from what the
//  moc of Qt 6.12.0 writes for its header: Qt's library keeps it to itself;
//  added are 2 rituals that lean on what moc writes for a class of the part
//  Qt keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/menuactionlineedit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only WITH Qt-GPL-exception-1.0
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtDesigner__qdesigner_internal_MenuActionLineEdit.cpp, line 1, as moc:qdesigner_internal::MenuActionLineEdit
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN18qdesigner_internal18MenuActionLineEditE_t {};
} // unnamed namespace

template <> constexpr inline auto qdesigner_internal::MenuActionLineEdit::qt_create_metaobjectdata<qt_meta_tag_ZN18qdesigner_internal18MenuActionLineEditE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "qdesigner_internal::MenuActionLineEdit",
        "focusOut",
        ""
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'focusOut'
        QtMocHelpers::SignalData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<MenuActionLineEdit, qt_meta_tag_ZN18qdesigner_internal18MenuActionLineEditE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject qdesigner_internal::MenuActionLineEdit::staticMetaObject = { {
    QMetaObject::SuperData::link<QLineEdit::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18qdesigner_internal18MenuActionLineEditE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18qdesigner_internal18MenuActionLineEditE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN18qdesigner_internal18MenuActionLineEditE_t>.metaTypes,
    nullptr
} };

void qdesigner_internal::MenuActionLineEdit::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<MenuActionLineEdit *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->focusOut(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (MenuActionLineEdit::*)()>(_a, &MenuActionLineEdit::focusOut, 0))
            return;
    }
}

const QMetaObject *qdesigner_internal::MenuActionLineEdit::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *qdesigner_internal::MenuActionLineEdit::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18qdesigner_internal18MenuActionLineEditE_t>.strings))
        return static_cast<void*>(this);
    return QLineEdit::qt_metacast(_clname);
}

int qdesigner_internal::MenuActionLineEdit::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QLineEdit::qt_metacall(_c, _id, _a);
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

// SIGNAL 0
void qdesigner_internal::MenuActionLineEdit::focusOut()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}
QT_WARNING_POP
//  -----------------------------------------------------------------------

//  Only a class built on qdesigner_internal::MenuActionLineEdit may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct Ownqdesigner_internal_MenuActionLineEdit : qdesigner_internal::MenuActionLineEdit {
  using qdesigner_internal::MenuActionLineEdit::focusOutEvent;
};

//  A qdesigner_internal::MenuActionLineEdit that Python can take functions over in. Every qdesigner_internal::MenuActionLineEdit
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall0)(const void *, QFocusEvent *, int *);
#if QT_CONFIG(lineedit)
typedef const QSize * (*Cuteqdesigner_internal_MenuActionLineEditCall1)(const void *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef const QSize * (*Cuteqdesigner_internal_MenuActionLineEditCall2)(const void *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall3)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall4)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall5)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall6)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall7)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall8)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall9)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall10)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall11)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall12)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall13)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall14)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall15)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(lineedit)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall16)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(lineedit)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall17)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall18)(const void *, QStyleOptionFrame *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef const QVariant * (*Cuteqdesigner_internal_MenuActionLineEditCall19)(const void *, int, int *);
#endif  // QT_CONFIG(lineedit)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(lineedit)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall20)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(lineedit)
typedef bool (*Cuteqdesigner_internal_MenuActionLineEditCall21)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*Cuteqdesigner_internal_MenuActionLineEditCall22)(const void *, int *);
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall23)(const void *, bool, int *);
typedef int (*Cuteqdesigner_internal_MenuActionLineEditCall24)(const void *, int, int *);
typedef bool (*Cuteqdesigner_internal_MenuActionLineEditCall25)(const void *, int *);
typedef void * (*Cuteqdesigner_internal_MenuActionLineEditCall26)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall27)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall28)(const void *, QEnterEvent *, int *);
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall29)(const void *, QEvent *, int *);
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall30)(const void *, QMoveEvent *, int *);
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall31)(const void *, QResizeEvent *, int *);
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall32)(const void *, QCloseEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall33)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall34)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall35)(const void *, QShowEvent *, int *);
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall36)(const void *, QHideEvent *, int *);
typedef int (*Cuteqdesigner_internal_MenuActionLineEditCall37)(const void *, int, int *);
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall38)(const void *, QPainter *, int *);
typedef void * (*Cuteqdesigner_internal_MenuActionLineEditCall39)(const void *, QPoint *, int *);
typedef void * (*Cuteqdesigner_internal_MenuActionLineEditCall40)(const void *, int *);
typedef bool (*Cuteqdesigner_internal_MenuActionLineEditCall41)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_MenuActionLineEditCall42)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall43)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall44)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_MenuActionLineEditCall46)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class Cuteqdesigner_internal_MenuActionLineEdit : public qdesigner_internal::MenuActionLineEdit {
public:
  using qdesigner_internal::MenuActionLineEdit::MenuActionLineEdit;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[0] = call;
      return true;
    }
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZNK9QLineEdit15initStyleOptionEP17QStyleOptionFrame")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[26] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[32] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[41] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[46] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void
  //      qdesigner_internal::MenuActionLineEdit::focusOutEvent(QFocusEvent
  //      *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall0 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    qdesigner_internal::MenuActionLineEdit::focusOutEvent(event);
  }

#if QT_CONFIG(lineedit)
  //  QSize QLineEdit::sizeHint() const
  QSize sizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall1 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLineEdit::sizeHint();
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  QSize QLineEdit::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall2 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLineEdit::minimumSizeHint();
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall3 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::mousePressEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall4 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::mouseMoveEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall5 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::mouseReleaseEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::mouseDoubleClickEvent(QMouseEvent *a0)
  void mouseDoubleClickEvent(QMouseEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall6 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::mouseDoubleClickEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall7 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::keyPressEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall8 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::keyReleaseEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall9 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::focusInEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall10 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::paintEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
  //  void QLineEdit::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall11 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
  //  void QLineEdit::dragMoveEvent(QDragMoveEvent *e)
  void dragMoveEvent(QDragMoveEvent *e) override {
    if (taken[12]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall12 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall12>(taken[12]);
      call(this, e, &handled);
      if (handled) return;
    }
    QLineEdit::dragMoveEvent(e);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
  //  void QLineEdit::dragLeaveEvent(QDragLeaveEvent *e)
  void dragLeaveEvent(QDragLeaveEvent *e) override {
    if (taken[13]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall13 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall13>(taken[13]);
      call(this, e, &handled);
      if (handled) return;
    }
    QLineEdit::dragLeaveEvent(e);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
  //  void QLineEdit::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall14 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::dropEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall15 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::changeEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(lineedit)
  //  void QLineEdit::contextMenuEvent(QContextMenuEvent *a0)
  void contextMenuEvent(QContextMenuEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall16 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::contextMenuEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall17 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[18]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall18 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall18>(taken[18]);
      call(this, option, &handled);
      if (handled) return;
    }
    QLineEdit::initStyleOption(option);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  QVariant QLineEdit::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[19]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall19 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall19>(taken[19]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QLineEdit::inputMethodQuery(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(lineedit)
  //  void QLineEdit::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall20 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::timerEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(lineedit)
  //  bool QLineEdit::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall21 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall21>(taken[21]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLineEdit::event(a0);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // !defined(QT_NO_QOBJECT)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[22]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall22 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall22>(taken[22]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[23]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall23 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall23>(taken[23]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[24]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall24 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall24>(taken[24]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[25]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall25 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall25>(taken[25]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[26]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall26 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall26>(taken[26]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall27 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall28 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall29 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall30 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall31 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall32 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall33 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall34 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall35 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall36 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[37]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall37 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall37>(taken[37]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[38]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall38 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall38>(taken[38]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[39]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall39 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall39>(taken[39]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[40]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall40 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall40>(taken[40]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[41]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall41 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall41>(taken[41]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall42 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall42>(taken[42]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall43 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall44 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall45 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[46]) {
      int handled = 0;
      Cuteqdesigner_internal_MenuActionLineEditCall46 call = reinterpret_cast<Cuteqdesigner_internal_MenuActionLineEditCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *qdesigner_internal::MenuActionLineEdit::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal18MenuActionLineEdit10metaObjectEv(
    const qdesigner_internal::MenuActionLineEdit *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::MenuActionLineEdit::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal18MenuActionLineEdit11qt_metacastEPKc(
    qdesigner_internal::MenuActionLineEdit *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::MenuActionLineEdit::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal18MenuActionLineEdit11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::MenuActionLineEdit *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString qdesigner_internal::MenuActionLineEdit::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal18MenuActionLineEdit2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::MenuActionLineEdit::tr(s, c, n));
}

//  void qdesigner_internal::MenuActionLineEdit::focusOut()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18MenuActionLineEdit8focusOutEv(
    qdesigner_internal::MenuActionLineEdit *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::MenuActionLineEdit")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "focusOut()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "focusOut()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::MenuActionLineEdit::focusOutEvent(QFocusEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18MenuActionLineEdit13focusOutEventEP11QFocusEvent(
    qdesigner_internal::MenuActionLineEdit *self,
    QFocusEvent *event) {
  self->focusOutEvent(event);
}

//  a Python function taken by a Cuteqdesigner_internal_MenuActionLineEdit,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_MenuActionLineEdit(
    qdesigner_internal::MenuActionLineEdit *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_MenuActionLineEdit *>(self)->take(key, call);
}

//  void qdesigner_internal::MenuActionLineEdit::focusOutEvent(QFocusEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal18MenuActionLineEdit13focusOutEventEP11QFocusEvent(
    qdesigner_internal::MenuActionLineEdit *self,
    QFocusEvent *event) {
  static_cast<Ownqdesigner_internal_MenuActionLineEdit *>(self)->Ownqdesigner_internal_MenuActionLineEdit::focusOutEvent(
      event);
}
