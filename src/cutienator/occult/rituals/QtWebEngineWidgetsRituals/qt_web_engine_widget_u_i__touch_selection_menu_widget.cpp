//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineWid
//  gets/6.12.0/QtWebEngineWidgets/private/touchselectionmenuwidget_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtWebEngineWidgets/QtWebEngineWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineWidgets/6.12.0/QtWebEngineWidgets/private/touchselectionmenuwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
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

//  from ../qtwebengine/src/webenginewidgets/ui/touchselectionmenuwidget.cpp, line 110, as _ZN19QtWebEngineWidgetUI24TouchSelectionMenuWidget11eventFilterEP7QObjectP6QEvent
namespace QtWebEngineWidgetUI {
inline bool TouchSelectionMenuWidget::eventFilter(QObject *obj, QEvent *ev)
{
    // Close the menu if the window is moved
    if (ev->type() == QEvent::Move)
        close();

    return QWidget::eventFilter(obj, ev);
}
}  // namespace QtWebEngineWidgetUI

//  from ../qtwebengine/src/webenginewidgets/ui/touchselectionmenuwidget.cpp, line 106, as _ZN19QtWebEngineWidgetUI24TouchSelectionMenuWidgetD1Ev
namespace QtWebEngineWidgetUI {
inline TouchSelectionMenuWidget::~TouchSelectionMenuWidget()
{
}
}  // namespace QtWebEngineWidgetUI
//  -----------------------------------------------------------------------

//  Only a class built on QtWebEngineWidgetUI::TouchSelectionMenuWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQtWebEngineWidgetUI_TouchSelectionMenuWidget : QtWebEngineWidgetUI::TouchSelectionMenuWidget {
  using QtWebEngineWidgetUI::TouchSelectionMenuWidget::eventFilter;
};

//  A QtWebEngineWidgetUI::TouchSelectionMenuWidget that Python can take functions over in. Every QtWebEngineWidgetUI::TouchSelectionMenuWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall0)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall1)(const void *, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall2)(const void *, bool, int *);
typedef const QSize * (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall3)(const void *, int *);
typedef const QSize * (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall4)(const void *, int *);
typedef int (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall5)(const void *, int, int *);
typedef bool (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall6)(const void *, int *);
typedef void * (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall9)(const void *, QMouseEvent *, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall10)(const void *, QMouseEvent *, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall12)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall13)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall18)(const void *, QEnterEvent *, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall19)(const void *, QEvent *, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall20)(const void *, QPaintEvent *, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall21)(const void *, QMoveEvent *, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall22)(const void *, QResizeEvent *, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall23)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall24)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall25)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall26)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall27)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall28)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall29)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall30)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall31)(const void *, QShowEvent *, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall32)(const void *, QHideEvent *, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall33)(const void *, QEvent *, int *);
typedef int (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall34)(const void *, int, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall35)(const void *, QPainter *, int *);
typedef void * (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall36)(const void *, QPoint *, int *);
typedef void * (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall37)(const void *, int *);
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall38)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall39)(const void *, int, int *);
typedef bool (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall40)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall41)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall42)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall43)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget : public QtWebEngineWidgetUI::TouchSelectionMenuWidget {
public:
  using QtWebEngineWidgetUI::TouchSelectionMenuWidget::TouchSelectionMenuWidget;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[23] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[40] = call;
      return true;
    }
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

#if !defined(QT_NO_QOBJECT)
  //  bool
  //      QtWebEngineWidgetUI::TouchSelectionMenuWidget::eventFilter(QObjec
  //      t *obj, QEvent *ev)
  bool eventFilter(QObject *obj, QEvent *ev) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall0 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall0>(taken[0]);
      bool given = call(this, obj, ev, &handled);
      if (handled) return given;
    }
    return QtWebEngineWidgetUI::TouchSelectionMenuWidget::eventFilter(obj, ev);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall1 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[2]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall2 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall2>(taken[2]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall3 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall4 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall5 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall5>(taken[5]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall6 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall7 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall8 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall9 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall10 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall11 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall12 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall13 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall13>(taken[13]);
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
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall14 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall15 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall16 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall17 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall18 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall19 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall20 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall21 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall22 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall23 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall24 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall25 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall26 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall27 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall28 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall29 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall30 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall31 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall32 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall33 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall34 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall34>(taken[34]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall35 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall35>(taken[35]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall36 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall36>(taken[36]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall37 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall37>(taken[37]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall38 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall39 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall39>(taken[39]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[40]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall40 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall40>(taken[40]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall41 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall41>(taken[41]);
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
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall42 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall42>(taken[42]);
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
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall43 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall43>(taken[43]);
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
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall44 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall44>(taken[44]);
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
      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall45 call = reinterpret_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidgetCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QtWebEngineWidgetUI::TouchSelectionMenuWidget::~TouchSelectionMenuWidget(
//      )
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtWebEngineWidgetUI24TouchSelectionMenuWidgetD1Ev(
    QtWebEngineWidgetUI::TouchSelectionMenuWidget *self) {
  delete self;
}

//  bool QtWebEngineWidgetUI::TouchSelectionMenuWidget::eventFilter(QObject
//      *obj, QEvent *ev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QtWebEngineWidgetUI24TouchSelectionMenuWidget11eventFilterEP7QObjectP6QEvent(
    QtWebEngineWidgetUI::TouchSelectionMenuWidget *self,
    QObject *obj,
    QEvent *ev) {
  return self->eventFilter(obj, ev);
}

//  a Python function taken by a
//      CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtWebEngineWidgetUI_TouchSelectionMenuWidget(
    QtWebEngineWidgetUI::TouchSelectionMenuWidget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtWebEngineWidgetUI_TouchSelectionMenuWidget *>(self)->take(key, call);
}

//  bool QtWebEngineWidgetUI::TouchSelectionMenuWidget::eventFilter(QObject
//      *obj, QEvent *ev)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QtWebEngineWidgetUI24TouchSelectionMenuWidget11eventFilterEP7QObjectP6QEvent(
    QtWebEngineWidgetUI::TouchSelectionMenuWidget *self,
    QObject *obj,
    QEvent *ev) {
  return static_cast<OwnQtWebEngineWidgetUI_TouchSelectionMenuWidget *>(self)->OwnQtWebEngineWidgetUI_TouchSelectionMenuWidget::eventFilter(
      obj,
      ev);
}
