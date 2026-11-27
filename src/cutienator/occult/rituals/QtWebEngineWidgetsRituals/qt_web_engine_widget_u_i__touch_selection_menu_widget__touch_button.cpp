//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineWid
//  gets/6.12.0/QtWebEngineWidgets/private/touchselectionmenuwidget_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtWebEngineWidgets/QtWebEngineWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineWidgets/6.12.0/QtWebEngineWidgets/private/touchselectionmenuwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineWidgets/private/touchselectionmenuwidget_p.h>
#include <QtWebEngineWidgets/qwebengineview.h>
#include <QtWidgets/QBoxLayout>
#include <QtCore/QEvent>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwebengine/src/webenginewidgets/ui/touchselectionmenuwidget.cpp, line 35, as _ZN19QtWebEngineWidgetUI24TouchSelectionMenuWidget11TouchButton5eventEP6QEvent
namespace QtWebEngineWidgetUI {
inline bool TouchSelectionMenuWidget::TouchButton::event(QEvent *ev)
{
    switch (ev->type()) {
    case QEvent::TouchBegin:
        ev->accept();
        return true;
    case QEvent::TouchEnd:
        Q_EMIT clicked();
        ev->accept();
        return true;
    default:
        break;
    }

    return QPushButton::event(ev);
}
}  // namespace QtWebEngineWidgetUI

//  from ../qtwebengine/src/webenginewidgets/ui/touchselectionmenuwidget.cpp, line 25, as _ZN19QtWebEngineWidgetUI24TouchSelectionMenuWidget11TouchButtonC1E7QStringP7QWidget
namespace QtWebEngineWidgetUI {
inline TouchSelectionMenuWidget::TouchButton::TouchButton(QString name, QWidget *parent)
    : QPushButton(name, parent)
{
    setAttribute(Qt::WA_AcceptTouchEvents, true);
}
}  // namespace QtWebEngineWidgetUI

//  from ../qtwebengine/src/webenginewidgets/ui/touchselectionmenuwidget.cpp, line 31, as _ZN19QtWebEngineWidgetUI24TouchSelectionMenuWidget11TouchButtonD1Ev
namespace QtWebEngineWidgetUI {
inline TouchSelectionMenuWidget::TouchButton::~TouchButton()
{
}
}  // namespace QtWebEngineWidgetUI
//  -----------------------------------------------------------------------

//  Only a class built on QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButton : QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton {
  using QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton::event;
};

//  A QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton that Python can take functions over in. Every QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(pushbutton)
typedef const QSize * (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall1)(const void *, int *);
#endif  // QT_CONFIG(pushbutton)
#if QT_CONFIG(pushbutton)
typedef const QSize * (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall2)(const void *, int *);
#endif  // QT_CONFIG(pushbutton)
#if QT_CONFIG(pushbutton)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall3)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(pushbutton)
#if QT_CONFIG(pushbutton)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall4)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(pushbutton)
#if QT_CONFIG(pushbutton)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall5)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(pushbutton)
#if QT_CONFIG(pushbutton)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall6)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(pushbutton)
#if QT_CONFIG(pushbutton)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall7)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(pushbutton)
#if QT_CONFIG(pushbutton)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall8)(const void *, QStyleOptionButton *, int *);
#endif  // QT_CONFIG(pushbutton)
#if QT_CONFIG(abstractbutton)
#if QT_CONFIG(pushbutton)
typedef bool (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall9)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(pushbutton)
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall10)(const void *, int *);
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall11)(const void *, int *);
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall12)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall13)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall14)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall15)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(abstractbutton)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(abstractbutton)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall16)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(abstractbutton)
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall17)(const void *, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall18)(const void *, bool, int *);
typedef int (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall19)(const void *, int, int *);
typedef bool (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall20)(const void *, int *);
typedef void * (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall21)(const void *, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall22)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall23)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall24)(const void *, QEnterEvent *, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall25)(const void *, QEvent *, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall26)(const void *, QMoveEvent *, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall27)(const void *, QResizeEvent *, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall28)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall29)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall30)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall31)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall32)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall33)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall34)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall35)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall36)(const void *, QShowEvent *, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall37)(const void *, QHideEvent *, int *);
typedef int (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall38)(const void *, int, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall39)(const void *, QPainter *, int *);
typedef void * (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall40)(const void *, QPoint *, int *);
typedef void * (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall41)(const void *, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall42)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall43)(const void *, int, int *);
typedef bool (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall44)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall45)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall46)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall47)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall48)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall49)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButton : public QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton {
public:
  using QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton::TouchButton;
  void *taken[50] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(pushbutton)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(pushbutton)
#if QT_CONFIG(pushbutton)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(pushbutton)
#if QT_CONFIG(pushbutton)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(pushbutton)
#if QT_CONFIG(pushbutton)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(pushbutton)
#if QT_CONFIG(pushbutton)
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(pushbutton)
#if QT_CONFIG(pushbutton)
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(pushbutton)
#if QT_CONFIG(pushbutton)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(pushbutton)
#if QT_CONFIG(pushbutton)
    if (!std::strcmp(key, "_ZNK11QPushButton15initStyleOptionEP18QStyleOptionButton")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(pushbutton)
#if QT_CONFIG(abstractbutton)
#if QT_CONFIG(pushbutton)
    if (!std::strcmp(key, "_ZNK15QAbstractButton9hitButtonERK6QPoint")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(pushbutton)
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZN15QAbstractButton13checkStateSetEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZN15QAbstractButton14nextCheckStateEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[28] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[44] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[49] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton::even
  //      t(QEvent *ev)
  bool event(QEvent *ev) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall0 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall0>(taken[0]);
      bool given = call(this, ev, &handled);
      if (handled) return given;
    }
    return QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton::event(ev);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(pushbutton)
  //  QSize QPushButton::sizeHint() const
  QSize sizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall1 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPushButton::sizeHint();
  }
#endif  // QT_CONFIG(pushbutton)

#if QT_CONFIG(pushbutton)
  //  QSize QPushButton::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall2 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPushButton::minimumSizeHint();
  }
#endif  // QT_CONFIG(pushbutton)

#if QT_CONFIG(pushbutton)
  //  void QPushButton::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall3 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPushButton::paintEvent(a0);
  }
#endif  // QT_CONFIG(pushbutton)

#if QT_CONFIG(pushbutton)
  //  void QPushButton::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall4 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPushButton::keyPressEvent(a0);
  }
#endif  // QT_CONFIG(pushbutton)

#if QT_CONFIG(pushbutton)
  //  void QPushButton::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall5 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPushButton::focusInEvent(a0);
  }
#endif  // QT_CONFIG(pushbutton)

#if QT_CONFIG(pushbutton)
  //  void QPushButton::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall6 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPushButton::focusOutEvent(a0);
  }
#endif  // QT_CONFIG(pushbutton)

#if QT_CONFIG(pushbutton)
  //  void QPushButton::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall7 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPushButton::mouseMoveEvent(a0);
  }
#endif  // QT_CONFIG(pushbutton)

#if QT_CONFIG(pushbutton)
  //  void QPushButton::initStyleOption(QStyleOptionButton *option) const
  void initStyleOption(QStyleOptionButton *option) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall8 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall8>(taken[8]);
      call(this, option, &handled);
      if (handled) return;
    }
    QPushButton::initStyleOption(option);
  }
#endif  // QT_CONFIG(pushbutton)

#if QT_CONFIG(abstractbutton)
#if QT_CONFIG(pushbutton)
  //  bool QPushButton::hitButton(const QPoint &pos) const
  bool hitButton(const QPoint &pos) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall9 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall9>(taken[9]);
      bool given = call(this, &pos, &handled);
      if (handled) return given;
    }
    return QPushButton::hitButton(pos);
  }
#endif  // QT_CONFIG(pushbutton)
#endif  // QT_CONFIG(abstractbutton)

#if QT_CONFIG(abstractbutton)
  //  void QAbstractButton::checkStateSet()
  void checkStateSet() override {
    if (taken[10]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall10 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractButton::checkStateSet();
  }
#endif  // QT_CONFIG(abstractbutton)

#if QT_CONFIG(abstractbutton)
  //  void QAbstractButton::nextCheckState()
  void nextCheckState() override {
    if (taken[11]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall11 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractButton::nextCheckState();
  }
#endif  // QT_CONFIG(abstractbutton)

#if QT_CONFIG(abstractbutton)
  //  void QAbstractButton::keyReleaseEvent(QKeyEvent *e)
  void keyReleaseEvent(QKeyEvent *e) override {
    if (taken[12]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall12 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall12>(taken[12]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::keyReleaseEvent(e);
  }
#endif  // QT_CONFIG(abstractbutton)

#if QT_CONFIG(abstractbutton)
  //  void QAbstractButton::mousePressEvent(QMouseEvent *e)
  void mousePressEvent(QMouseEvent *e) override {
    if (taken[13]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall13 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall13>(taken[13]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::mousePressEvent(e);
  }
#endif  // QT_CONFIG(abstractbutton)

#if QT_CONFIG(abstractbutton)
  //  void QAbstractButton::mouseReleaseEvent(QMouseEvent *e)
  void mouseReleaseEvent(QMouseEvent *e) override {
    if (taken[14]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall14 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall14>(taken[14]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::mouseReleaseEvent(e);
  }
#endif  // QT_CONFIG(abstractbutton)

#if QT_CONFIG(abstractbutton)
  //  void QAbstractButton::changeEvent(QEvent *e)
  void changeEvent(QEvent *e) override {
    if (taken[15]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall15 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall15>(taken[15]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::changeEvent(e);
  }
#endif  // QT_CONFIG(abstractbutton)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(abstractbutton)
  //  void QAbstractButton::timerEvent(QTimerEvent *e)
  void timerEvent(QTimerEvent *e) override {
    if (taken[16]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall16 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall16>(taken[16]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractButton::timerEvent(e);
  }
#endif  // QT_CONFIG(abstractbutton)
#endif  // !defined(QT_NO_QOBJECT)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall17 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[18]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall18 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall18>(taken[18]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall19 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall19>(taken[19]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall20 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall21 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall21>(taken[21]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall22 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall23 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall24 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall25 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall26 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall27 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall28 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall29 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall30 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall31 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall32 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall33 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall34 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall35 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall36 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall37 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall38 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall38>(taken[38]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall39 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall39>(taken[39]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall40 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall40>(taken[40]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[41]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall41 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall41>(taken[41]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall42 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall42>(taken[42]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[43]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall43 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall43>(taken[43]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[44]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall44 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall44>(taken[44]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall45 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall45>(taken[45]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall46 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall47 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[48]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall48 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall48>(taken[48]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[49]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall49 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButtonCall49>(taken[49]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton::TouchButton(Q
//      String name, QWidget *parent)
extern "C" Q_DECL_EXPORT
QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton *ritual_ZN19QtWebEngineWidgetUI24TouchSelectionMenuWidget11TouchButtonC1E7QStringP7QWidget(
    const QString *name,
    QWidget *parent) {
  return new CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButton(
      *name,
      parent);
}

//  QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton::~TouchButton(
//      )
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtWebEngineWidgetUI24TouchSelectionMenuWidget11TouchButtonD1Ev(
    QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton *self) {
  delete self;
}

//  bool
//      QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton::event(QEv
//      ent *ev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QtWebEngineWidgetUI24TouchSelectionMenuWidget11TouchButton5eventEP6QEvent(
    QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton *self,
    QEvent *ev) {
  return self->event(ev);
}

//  a Python function taken by a
//      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButton, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButton(
    QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButton *>(self)->take(key, call);
}

//  bool
//      QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton::event(QEv
//      ent *ev)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QtWebEngineWidgetUI24TouchSelectionMenuWidget11TouchButton5eventEP6QEvent(
    QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchButton *self,
    QEvent *ev) {
  return static_cast<OwnQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButton *>(self)->OwnQtWebEngineWidgetUI_TouchSelectionMenuWidget_TouchButton::event(
      ev);
}
