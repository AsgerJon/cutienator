//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcolumnviewgrip_p.h, Qt 6.12.0. Edited
//  by hand on 2026-11-26: moc's output for 'QColumnViewGrip' is pasted in,
//  cut from what the moc of Qt 6.12.0 writes for its header: Qt's library
//  keeps it to itself; added are 6 rituals that lean on what moc writes for
//  a class of the part Qt keeps to itself, whose ritual file carries moc's
//  output, drafted by a copy of the generator that lets those names through.
//  A copy of a meta-object is a second one: 'qobject_cast' between it and
//  Qt's own does not match. Edited by hand on 2026-11-27: the constructors
//  and the destructor of QColumnViewGrip taken from Qt are no longer
//  'inline' (3): the one definition the target file has of each, which the
//  ritual files of other classes of the part call, as Microsoft's ABI emits
//  an 'inline' one only where it is used. Kept as it is when the generator
//  runs again.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(columnview)
#if QT_CONFIG(columnview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qcolumnviewgrip_p.h>
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
#include <QtWidgets/private/qcolumnviewgrip_p.h>
#include <QtWidgets/qstyleoption.h>
#include <QtGui/qpainter.h>
#include <QtGui/qbrush.h>
#include <QtGui/qevent.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtWidgets__QColumnViewGrip.cpp, line 1, as moc:QColumnViewGrip
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN15QColumnViewGripE_t {};
} // unnamed namespace

template <> constexpr inline auto QColumnViewGrip::qt_create_metaobjectdata<qt_meta_tag_ZN15QColumnViewGripE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QColumnViewGrip",
        "gripMoved",
        "",
        "offset"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'gripMoved'
        QtMocHelpers::SignalData<void(int)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Int, 3 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QColumnViewGrip, qt_meta_tag_ZN15QColumnViewGripE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QColumnViewGrip::staticMetaObject = { {
    QMetaObject::SuperData::link<QWidget::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15QColumnViewGripE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15QColumnViewGripE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN15QColumnViewGripE_t>.metaTypes,
    nullptr
} };

void QColumnViewGrip::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QColumnViewGrip *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->gripMoved((*reinterpret_cast<std::add_pointer_t<int>>(_a[1]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QColumnViewGrip::*)(int )>(_a, &QColumnViewGrip::gripMoved, 0))
            return;
    }
}

const QMetaObject *QColumnViewGrip::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QColumnViewGrip::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15QColumnViewGripE_t>.strings))
        return static_cast<void*>(this);
    return QWidget::qt_metacast(_clname);
}

int QColumnViewGrip::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
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
void QColumnViewGrip::gripMoved(int _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1);
}
QT_WARNING_POP

//  from src/widgets/itemviews/qcolumnviewgrip.cpp, line 85, as _ZN15QColumnViewGrip10paintEventEP11QPaintEvent
inline void QColumnViewGrip::paintEvent(QPaintEvent *event)
{
    QPainter painter(this);
    QStyleOption opt;
    opt.initFrom(this);
    style()->drawControl(QStyle::CE_ColumnViewGrip, &opt, &painter, this);
    event->accept();
}

//  from src/widgets/itemviews/qcolumnviewgrip.cpp, line 124, as _ZN15QColumnViewGrip14mouseMoveEventEP11QMouseEvent
inline void QColumnViewGrip::mouseMoveEvent(QMouseEvent *event)
{
    Q_D(QColumnViewGrip);
    int offset = event->globalPosition().toPoint().x() - d->originalXLocation;
    d->originalXLocation = moveGrip(offset) + d->originalXLocation;
    event->accept();
}

//  from src/widgets/itemviews/qcolumnviewgrip.cpp, line 113, as _ZN15QColumnViewGrip15mousePressEventEP11QMouseEvent
inline void QColumnViewGrip::mousePressEvent(QMouseEvent *event)
{
    Q_D(QColumnViewGrip);
    d->originalXLocation = event->globalPosition().toPoint().x();
    event->accept();
}

//  from src/widgets/itemviews/qcolumnviewgrip.cpp, line 136, as _ZN15QColumnViewGrip17mouseReleaseEventEP11QMouseEvent
inline void QColumnViewGrip::mouseReleaseEvent(QMouseEvent *event)
{
    Q_D(QColumnViewGrip);
    d->originalXLocation = -1;
    event->accept();
}

//  from src/widgets/itemviews/qcolumnviewgrip.cpp, line 98, as _ZN15QColumnViewGrip21mouseDoubleClickEventEP11QMouseEvent
inline void QColumnViewGrip::mouseDoubleClickEvent(QMouseEvent *event)
{
    Q_UNUSED(event);
    QWidget *parentWidget = (QWidget*)parent();
    int offset = parentWidget->sizeHint().width() - parentWidget->width();
    if (isRightToLeft())
        offset *= -1;
    moveGrip(offset);
    event->accept();
}

//  from src/widgets/itemviews/qcolumnviewgrip.cpp, line 146, as _ZN22QColumnViewGripPrivateC1Ev
inline QColumnViewGripPrivate::QColumnViewGripPrivate()
:  QWidgetPrivate(),
originalXLocation(-1)
{
}

//  from src/widgets/itemviews/qcolumnviewgrip.cpp, line 31, as _ZN15QColumnViewGripC1EP7QWidget
QColumnViewGrip::QColumnViewGrip(QWidget *parent)
    :  QWidget(*new QColumnViewGripPrivate, parent, { })
{
#ifndef QT_NO_CURSOR
    setCursor(Qt::SplitHCursor);
#endif
}

//  from src/widgets/itemviews/qcolumnviewgrip.cpp, line 50, as _ZN15QColumnViewGripD1Ev
QColumnViewGrip::~QColumnViewGrip()
{
}

//  from src/widgets/itemviews/qcolumnviewgrip.cpp, line 58, as _ZN15QColumnViewGrip8moveGripEi
inline int QColumnViewGrip::moveGrip(int offset)
{
    QWidget *parentWidget = (QWidget*)parent();

    // first resize the parent
    int oldWidth = parentWidget->width();
    int newWidth = oldWidth;
    if (isRightToLeft())
       newWidth -= offset;
    else
       newWidth += offset;
    newWidth = qMax(parentWidget->minimumWidth(), newWidth);
    parentWidget->resize(newWidth, parentWidget->height());

    // Then have the view move the widget
    int realOffset = parentWidget->width() - oldWidth;
    int oldX = parentWidget->x();
    if (realOffset != 0)
        emit gripMoved(realOffset);
    if (isRightToLeft())
        realOffset = -1 * (oldX - parentWidget->x());
    return realOffset;
}

//  from src/widgets/itemviews/qcolumnviewgrip.cpp, line 42, as _ZN15QColumnViewGripC1ER22QColumnViewGripPrivateP7QWidget6QFlagsIN2Qt10WindowTypeEE
QColumnViewGrip::QColumnViewGrip(QColumnViewGripPrivate & dd, QWidget *parent, Qt::WindowFlags f)
:  QWidget(dd, parent, f)
{
}
//  -----------------------------------------------------------------------

//  Only a class built on QColumnViewGrip may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQColumnViewGrip : QColumnViewGrip {
  using QColumnViewGrip::paintEvent;
  using QColumnViewGrip::mouseDoubleClickEvent;
  using QColumnViewGrip::mouseMoveEvent;
  using QColumnViewGrip::mouseReleaseEvent;
  using QColumnViewGrip::mousePressEvent;
};

//  A QColumnViewGrip that Python can take functions over in. Every QColumnViewGrip
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(columnview)
typedef void (*CuteQColumnViewGripCall0)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(columnview)
#if QT_CONFIG(columnview)
typedef void (*CuteQColumnViewGripCall1)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(columnview)
#if QT_CONFIG(columnview)
typedef void (*CuteQColumnViewGripCall2)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(columnview)
#if QT_CONFIG(columnview)
typedef void (*CuteQColumnViewGripCall3)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(columnview)
#if QT_CONFIG(columnview)
typedef void (*CuteQColumnViewGripCall4)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(columnview)
typedef int (*CuteQColumnViewGripCall5)(const void *, int *);
typedef void (*CuteQColumnViewGripCall6)(const void *, bool, int *);
typedef const QSize * (*CuteQColumnViewGripCall7)(const void *, int *);
typedef const QSize * (*CuteQColumnViewGripCall8)(const void *, int *);
typedef int (*CuteQColumnViewGripCall9)(const void *, int, int *);
typedef bool (*CuteQColumnViewGripCall10)(const void *, int *);
typedef void * (*CuteQColumnViewGripCall11)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQColumnViewGripCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(wheelevent)
typedef void (*CuteQColumnViewGripCall13)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQColumnViewGripCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQColumnViewGripCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQColumnViewGripCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQColumnViewGripCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQColumnViewGripCall18)(const void *, QEnterEvent *, int *);
typedef void (*CuteQColumnViewGripCall19)(const void *, QEvent *, int *);
typedef void (*CuteQColumnViewGripCall20)(const void *, QMoveEvent *, int *);
typedef void (*CuteQColumnViewGripCall21)(const void *, QResizeEvent *, int *);
typedef void (*CuteQColumnViewGripCall22)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQColumnViewGripCall23)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQColumnViewGripCall24)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQColumnViewGripCall25)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQColumnViewGripCall26)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQColumnViewGripCall27)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQColumnViewGripCall28)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQColumnViewGripCall29)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQColumnViewGripCall30)(const void *, QShowEvent *, int *);
typedef void (*CuteQColumnViewGripCall31)(const void *, QHideEvent *, int *);
typedef void (*CuteQColumnViewGripCall32)(const void *, QEvent *, int *);
typedef int (*CuteQColumnViewGripCall33)(const void *, int, int *);
typedef void (*CuteQColumnViewGripCall34)(const void *, QPainter *, int *);
typedef void * (*CuteQColumnViewGripCall35)(const void *, QPoint *, int *);
typedef void * (*CuteQColumnViewGripCall36)(const void *, int *);
typedef void (*CuteQColumnViewGripCall37)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQColumnViewGripCall38)(const void *, int, int *);
typedef bool (*CuteQColumnViewGripCall39)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQColumnViewGripCall40)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQColumnViewGripCall41)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQColumnViewGripCall42)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQColumnViewGripCall43)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQColumnViewGripCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQColumnViewGripCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQColumnViewGrip : public QColumnViewGrip {
public:
  using QColumnViewGrip::QColumnViewGrip;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(columnview)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(columnview)
#if QT_CONFIG(columnview)
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(columnview)
#if QT_CONFIG(columnview)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(columnview)
#if QT_CONFIG(columnview)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(columnview)
#if QT_CONFIG(columnview)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(columnview)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[11] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[22] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[39] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(columnview)
  //  void QColumnViewGrip::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQColumnViewGripCall0 call = reinterpret_cast<CuteQColumnViewGripCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QColumnViewGrip::paintEvent(event);
  }
#endif  // QT_CONFIG(columnview)

#if QT_CONFIG(columnview)
  //  void QColumnViewGrip::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQColumnViewGripCall1 call = reinterpret_cast<CuteQColumnViewGripCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QColumnViewGrip::mouseDoubleClickEvent(event);
  }
#endif  // QT_CONFIG(columnview)

#if QT_CONFIG(columnview)
  //  void QColumnViewGrip::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQColumnViewGripCall2 call = reinterpret_cast<CuteQColumnViewGripCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QColumnViewGrip::mouseMoveEvent(event);
  }
#endif  // QT_CONFIG(columnview)

#if QT_CONFIG(columnview)
  //  void QColumnViewGrip::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQColumnViewGripCall3 call = reinterpret_cast<CuteQColumnViewGripCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QColumnViewGrip::mouseReleaseEvent(event);
  }
#endif  // QT_CONFIG(columnview)

#if QT_CONFIG(columnview)
  //  void QColumnViewGrip::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQColumnViewGripCall4 call = reinterpret_cast<CuteQColumnViewGripCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QColumnViewGrip::mousePressEvent(event);
  }
#endif  // QT_CONFIG(columnview)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQColumnViewGripCall5 call = reinterpret_cast<CuteQColumnViewGripCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[6]) {
      int handled = 0;
      CuteQColumnViewGripCall6 call = reinterpret_cast<CuteQColumnViewGripCall6>(taken[6]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQColumnViewGripCall7 call = reinterpret_cast<CuteQColumnViewGripCall7>(taken[7]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQColumnViewGripCall8 call = reinterpret_cast<CuteQColumnViewGripCall8>(taken[8]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQColumnViewGripCall9 call = reinterpret_cast<CuteQColumnViewGripCall9>(taken[9]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQColumnViewGripCall10 call = reinterpret_cast<CuteQColumnViewGripCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQColumnViewGripCall11 call = reinterpret_cast<CuteQColumnViewGripCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQColumnViewGripCall12 call = reinterpret_cast<CuteQColumnViewGripCall12>(taken[12]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQColumnViewGripCall13 call = reinterpret_cast<CuteQColumnViewGripCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQColumnViewGripCall14 call = reinterpret_cast<CuteQColumnViewGripCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQColumnViewGripCall15 call = reinterpret_cast<CuteQColumnViewGripCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQColumnViewGripCall16 call = reinterpret_cast<CuteQColumnViewGripCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQColumnViewGripCall17 call = reinterpret_cast<CuteQColumnViewGripCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQColumnViewGripCall18 call = reinterpret_cast<CuteQColumnViewGripCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQColumnViewGripCall19 call = reinterpret_cast<CuteQColumnViewGripCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQColumnViewGripCall20 call = reinterpret_cast<CuteQColumnViewGripCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQColumnViewGripCall21 call = reinterpret_cast<CuteQColumnViewGripCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQColumnViewGripCall22 call = reinterpret_cast<CuteQColumnViewGripCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQColumnViewGripCall23 call = reinterpret_cast<CuteQColumnViewGripCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQColumnViewGripCall24 call = reinterpret_cast<CuteQColumnViewGripCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQColumnViewGripCall25 call = reinterpret_cast<CuteQColumnViewGripCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQColumnViewGripCall26 call = reinterpret_cast<CuteQColumnViewGripCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQColumnViewGripCall27 call = reinterpret_cast<CuteQColumnViewGripCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQColumnViewGripCall28 call = reinterpret_cast<CuteQColumnViewGripCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQColumnViewGripCall29 call = reinterpret_cast<CuteQColumnViewGripCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQColumnViewGripCall30 call = reinterpret_cast<CuteQColumnViewGripCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQColumnViewGripCall31 call = reinterpret_cast<CuteQColumnViewGripCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQColumnViewGripCall32 call = reinterpret_cast<CuteQColumnViewGripCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[33]) {
      int handled = 0;
      CuteQColumnViewGripCall33 call = reinterpret_cast<CuteQColumnViewGripCall33>(taken[33]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQColumnViewGripCall34 call = reinterpret_cast<CuteQColumnViewGripCall34>(taken[34]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQColumnViewGripCall35 call = reinterpret_cast<CuteQColumnViewGripCall35>(taken[35]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQColumnViewGripCall36 call = reinterpret_cast<CuteQColumnViewGripCall36>(taken[36]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQColumnViewGripCall37 call = reinterpret_cast<CuteQColumnViewGripCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQColumnViewGripCall38 call = reinterpret_cast<CuteQColumnViewGripCall38>(taken[38]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[39]) {
      int handled = 0;
      CuteQColumnViewGripCall39 call = reinterpret_cast<CuteQColumnViewGripCall39>(taken[39]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQColumnViewGripCall40 call = reinterpret_cast<CuteQColumnViewGripCall40>(taken[40]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQColumnViewGripCall41 call = reinterpret_cast<CuteQColumnViewGripCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQColumnViewGripCall42 call = reinterpret_cast<CuteQColumnViewGripCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQColumnViewGripCall43 call = reinterpret_cast<CuteQColumnViewGripCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[44]) {
      int handled = 0;
      CuteQColumnViewGripCall44 call = reinterpret_cast<CuteQColumnViewGripCall44>(taken[44]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQColumnViewGripCall45 call = reinterpret_cast<CuteQColumnViewGripCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QColumnViewGrip::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QColumnViewGrip10metaObjectEv(
    const QColumnViewGrip *self) {
  return self->metaObject();
}

//  void *QColumnViewGrip::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QColumnViewGrip11qt_metacastEPKc(
    QColumnViewGrip *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QColumnViewGrip::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QColumnViewGrip11qt_metacallEN11QMetaObject4CallEiPPv(
    QColumnViewGrip *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QColumnViewGrip::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QColumnViewGrip2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QColumnViewGrip::tr(s, c, n));
}

//  void QColumnViewGrip::gripMoved(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QColumnViewGrip9gripMovedEi(
    QColumnViewGrip *self,
    int offset) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QColumnViewGrip")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "gripMoved(int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "gripMoved(int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&offset)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QColumnViewGrip::QColumnViewGrip(QWidget *parent)
extern "C" Q_DECL_EXPORT
QColumnViewGrip *ritual_ZN15QColumnViewGripC1EP7QWidget(QWidget *parent) {
  return new CuteQColumnViewGrip(parent);
}

//  QColumnViewGrip::~QColumnViewGrip()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QColumnViewGripD1Ev(QColumnViewGrip *self) {
  delete self;
}

//  int QColumnViewGrip::moveGrip(int offset)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QColumnViewGrip8moveGripEi(
    QColumnViewGrip *self,
    int offset) {
  return self->moveGrip(offset);
}

//  QColumnViewGrip::QColumnViewGrip(QColumnViewGripPrivate &a0, QWidget
//      *parent, Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QColumnViewGrip *ritual_ZN15QColumnViewGripC1ER22QColumnViewGripPrivateP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QColumnViewGripPrivate *a0,
    QWidget *parent,
    int f) {
  return new CuteQColumnViewGrip(
      *a0,
      parent,
      QFlags<Qt::WindowType>::fromInt(f));
}

//  void QColumnViewGrip::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QColumnViewGrip10paintEventEP11QPaintEvent(
    QColumnViewGrip *self,
    QPaintEvent *event) {
  self->paintEvent(event);
}

//  void QColumnViewGrip::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QColumnViewGrip21mouseDoubleClickEventEP11QMouseEvent(
    QColumnViewGrip *self,
    QMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void QColumnViewGrip::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QColumnViewGrip14mouseMoveEventEP11QMouseEvent(
    QColumnViewGrip *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QColumnViewGrip::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QColumnViewGrip17mouseReleaseEventEP11QMouseEvent(
    QColumnViewGrip *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QColumnViewGrip::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QColumnViewGrip15mousePressEventEP11QMouseEvent(
    QColumnViewGrip *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  QColumnViewGripPrivate *QColumnViewGrip::d_func()
extern "C" Q_DECL_EXPORT
QColumnViewGripPrivate *ritual_ZN15QColumnViewGrip6d_funcEv(
    QColumnViewGrip *self) {
  return self->d_func();
}

//  const QColumnViewGripPrivate *QColumnViewGrip::d_func() const
extern "C" Q_DECL_EXPORT
const QColumnViewGripPrivate *ritual_ZNK15QColumnViewGrip6d_funcEv(
    const QColumnViewGrip *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQColumnViewGrip, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QColumnViewGrip(
    QColumnViewGrip *self,
    const char *key,
    void *call) {
  return static_cast<CuteQColumnViewGrip *>(self)->take(key, call);
}

//  void QColumnViewGrip::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QColumnViewGrip10paintEventEP11QPaintEvent(
    QColumnViewGrip *self,
    QPaintEvent *event) {
  static_cast<OwnQColumnViewGrip *>(self)->OwnQColumnViewGrip::paintEvent(
      event);
}

//  void QColumnViewGrip::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QColumnViewGrip21mouseDoubleClickEventEP11QMouseEvent(
    QColumnViewGrip *self,
    QMouseEvent *event) {
  static_cast<OwnQColumnViewGrip *>(self)->OwnQColumnViewGrip::mouseDoubleClickEvent(
      event);
}

//  void QColumnViewGrip::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QColumnViewGrip14mouseMoveEventEP11QMouseEvent(
    QColumnViewGrip *self,
    QMouseEvent *event) {
  static_cast<OwnQColumnViewGrip *>(self)->OwnQColumnViewGrip::mouseMoveEvent(
      event);
}

//  void QColumnViewGrip::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QColumnViewGrip17mouseReleaseEventEP11QMouseEvent(
    QColumnViewGrip *self,
    QMouseEvent *event) {
  static_cast<OwnQColumnViewGrip *>(self)->OwnQColumnViewGrip::mouseReleaseEvent(
      event);
}

//  void QColumnViewGrip::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QColumnViewGrip15mousePressEventEP11QMouseEvent(
    QColumnViewGrip *self,
    QMouseEvent *event) {
  static_cast<OwnQColumnViewGrip *>(self)->OwnQColumnViewGrip::mousePressEvent(
      event);
}

#endif  // QT_CONFIG(columnview)
#endif  // QT_CONFIG(columnview)
