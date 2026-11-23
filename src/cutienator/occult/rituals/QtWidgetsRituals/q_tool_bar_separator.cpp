//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtoolbarseparator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/QtWidgets>
#include <QtWidgets/6.12.0/QtWidgets/private/qtoolbarseparator_p.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include "qtoolbarseparator_p.h"
#include <qstyle.h>
#include <qstyleoption.h>
#include <qtoolbar.h>
#include <qpainter.h>

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it.

//  from src/widgets/widgets/qtoolbarseparator.cpp, line 34, as _ZNK17QToolBarSeparator8sizeHintEv
inline QSize QToolBarSeparator::sizeHint() const
{
    QStyleOption opt;
    initStyleOption(&opt);
    const int extent = style()->pixelMetric(QStyle::PM_ToolBarSeparatorExtent, &opt, parentWidget());
    return QSize(extent, extent);
}

//  from src/widgets/widgets/qtoolbarseparator.cpp, line 42, as _ZN17QToolBarSeparator10paintEventEP11QPaintEvent
inline void QToolBarSeparator::paintEvent(QPaintEvent *)
{
    QPainter p(this);
    QStyleOption opt;
    initStyleOption(&opt);
    style()->drawPrimitive(QStyle::PE_IndicatorToolBarSeparator, &opt, &p, parentWidget());
}

//  from src/widgets/widgets/qtoolbarseparator.cpp, line 25, as _ZN17QToolBarSeparator14setOrientationEN2Qt11OrientationE
inline void QToolBarSeparator::setOrientation(Qt::Orientation orientation)
{
    orient = orientation;
    update();
}
//  -----------------------------------------------------------------------

//  A QToolBarSeparator that Python can take functions over in. Every QToolBarSeparator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQToolBarSeparatorCall0)(const void *, int *);
typedef void (*CuteQToolBarSeparatorCall1)(const void *, QPaintEvent *, int *);
typedef int (*CuteQToolBarSeparatorCall2)(const void *, int *);
typedef void (*CuteQToolBarSeparatorCall3)(const void *, bool, int *);
typedef const QSize * (*CuteQToolBarSeparatorCall4)(const void *, int *);
typedef int (*CuteQToolBarSeparatorCall5)(const void *, int, int *);
typedef bool (*CuteQToolBarSeparatorCall6)(const void *, int *);
typedef void * (*CuteQToolBarSeparatorCall7)(const void *, int *);
typedef bool (*CuteQToolBarSeparatorCall8)(const void *, QEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall9)(const void *, QMouseEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall10)(const void *, QMouseEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall13)(const void *, QWheelEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall18)(const void *, QEnterEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall19)(const void *, QEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall20)(const void *, QMoveEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall21)(const void *, QResizeEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall22)(const void *, QCloseEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall23)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall24)(const void *, QTabletEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall25)(const void *, QActionEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall26)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall27)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall28)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall29)(const void *, QDropEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall30)(const void *, QShowEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall31)(const void *, QHideEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall32)(const void *, QEvent *, int *);
typedef int (*CuteQToolBarSeparatorCall33)(const void *, int, int *);
typedef void (*CuteQToolBarSeparatorCall34)(const void *, QPainter *, int *);
typedef void * (*CuteQToolBarSeparatorCall35)(const void *, QPoint *, int *);
typedef void * (*CuteQToolBarSeparatorCall36)(const void *, int *);
typedef void (*CuteQToolBarSeparatorCall37)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQToolBarSeparatorCall38)(const void *, int, int *);
typedef bool (*CuteQToolBarSeparatorCall39)(const void *, bool, int *);
typedef bool (*CuteQToolBarSeparatorCall40)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall41)(const void *, QTimerEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall42)(const void *, QChildEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall43)(const void *, QEvent *, int *);
typedef void (*CuteQToolBarSeparatorCall44)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQToolBarSeparatorCall45)(const void *, const QMetaMethod *, int *);
class CuteQToolBarSeparator : public QToolBarSeparator {
public:
  using QToolBarSeparator::QToolBarSeparator;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
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
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[13] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[29] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[45] = call;
      return true;
    }
    return false;
  }

  //  QSize QToolBarSeparator::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQToolBarSeparatorCall0 call = reinterpret_cast<CuteQToolBarSeparatorCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QToolBarSeparator::sizeHint();
  }

  //  void QToolBarSeparator::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQToolBarSeparatorCall1 call = reinterpret_cast<CuteQToolBarSeparatorCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QToolBarSeparator::paintEvent(a0);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQToolBarSeparatorCall2 call = reinterpret_cast<CuteQToolBarSeparatorCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[3]) {
      int handled = 0;
      CuteQToolBarSeparatorCall3 call = reinterpret_cast<CuteQToolBarSeparatorCall3>(taken[3]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQToolBarSeparatorCall4 call = reinterpret_cast<CuteQToolBarSeparatorCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQToolBarSeparatorCall5 call = reinterpret_cast<CuteQToolBarSeparatorCall5>(taken[5]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQToolBarSeparatorCall6 call = reinterpret_cast<CuteQToolBarSeparatorCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQToolBarSeparatorCall7 call = reinterpret_cast<CuteQToolBarSeparatorCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQToolBarSeparatorCall8 call = reinterpret_cast<CuteQToolBarSeparatorCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQToolBarSeparatorCall9 call = reinterpret_cast<CuteQToolBarSeparatorCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQToolBarSeparatorCall10 call = reinterpret_cast<CuteQToolBarSeparatorCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQToolBarSeparatorCall11 call = reinterpret_cast<CuteQToolBarSeparatorCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQToolBarSeparatorCall12 call = reinterpret_cast<CuteQToolBarSeparatorCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQToolBarSeparatorCall13 call = reinterpret_cast<CuteQToolBarSeparatorCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQToolBarSeparatorCall14 call = reinterpret_cast<CuteQToolBarSeparatorCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQToolBarSeparatorCall15 call = reinterpret_cast<CuteQToolBarSeparatorCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQToolBarSeparatorCall16 call = reinterpret_cast<CuteQToolBarSeparatorCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQToolBarSeparatorCall17 call = reinterpret_cast<CuteQToolBarSeparatorCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQToolBarSeparatorCall18 call = reinterpret_cast<CuteQToolBarSeparatorCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQToolBarSeparatorCall19 call = reinterpret_cast<CuteQToolBarSeparatorCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQToolBarSeparatorCall20 call = reinterpret_cast<CuteQToolBarSeparatorCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQToolBarSeparatorCall21 call = reinterpret_cast<CuteQToolBarSeparatorCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQToolBarSeparatorCall22 call = reinterpret_cast<CuteQToolBarSeparatorCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQToolBarSeparatorCall23 call = reinterpret_cast<CuteQToolBarSeparatorCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQToolBarSeparatorCall24 call = reinterpret_cast<CuteQToolBarSeparatorCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQToolBarSeparatorCall25 call = reinterpret_cast<CuteQToolBarSeparatorCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQToolBarSeparatorCall26 call = reinterpret_cast<CuteQToolBarSeparatorCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQToolBarSeparatorCall27 call = reinterpret_cast<CuteQToolBarSeparatorCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQToolBarSeparatorCall28 call = reinterpret_cast<CuteQToolBarSeparatorCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQToolBarSeparatorCall29 call = reinterpret_cast<CuteQToolBarSeparatorCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQToolBarSeparatorCall30 call = reinterpret_cast<CuteQToolBarSeparatorCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQToolBarSeparatorCall31 call = reinterpret_cast<CuteQToolBarSeparatorCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQToolBarSeparatorCall32 call = reinterpret_cast<CuteQToolBarSeparatorCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[33]) {
      int handled = 0;
      CuteQToolBarSeparatorCall33 call = reinterpret_cast<CuteQToolBarSeparatorCall33>(taken[33]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQToolBarSeparatorCall34 call = reinterpret_cast<CuteQToolBarSeparatorCall34>(taken[34]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQToolBarSeparatorCall35 call = reinterpret_cast<CuteQToolBarSeparatorCall35>(taken[35]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQToolBarSeparatorCall36 call = reinterpret_cast<CuteQToolBarSeparatorCall36>(taken[36]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQToolBarSeparatorCall37 call = reinterpret_cast<CuteQToolBarSeparatorCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQToolBarSeparatorCall38 call = reinterpret_cast<CuteQToolBarSeparatorCall38>(taken[38]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[39]) {
      int handled = 0;
      CuteQToolBarSeparatorCall39 call = reinterpret_cast<CuteQToolBarSeparatorCall39>(taken[39]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQToolBarSeparatorCall40 call = reinterpret_cast<CuteQToolBarSeparatorCall40>(taken[40]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQToolBarSeparatorCall41 call = reinterpret_cast<CuteQToolBarSeparatorCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQToolBarSeparatorCall42 call = reinterpret_cast<CuteQToolBarSeparatorCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQToolBarSeparatorCall43 call = reinterpret_cast<CuteQToolBarSeparatorCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[44]) {
      int handled = 0;
      CuteQToolBarSeparatorCall44 call = reinterpret_cast<CuteQToolBarSeparatorCall44>(taken[44]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQToolBarSeparatorCall45 call = reinterpret_cast<CuteQToolBarSeparatorCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QToolBarSeparator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QToolBarSeparator10metaObjectEv(
    const QToolBarSeparator *self) {
  return self->metaObject();
}

//  QSize QToolBarSeparator::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK17QToolBarSeparator8sizeHintEv(
    const QToolBarSeparator *self) {
  return new QSize(self->sizeHint());
}

//  void QToolBarSeparator::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QToolBarSeparator10paintEventEP11QPaintEvent(
    QToolBarSeparator *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

//  void QToolBarSeparator::setOrientation(Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QToolBarSeparator14setOrientationEN2Qt11OrientationE(
    QToolBarSeparator *self,
    Qt::Orientation orientation) {
  self->setOrientation(orientation);
}

//  a Python function taken by a CuteQToolBarSeparator, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QToolBarSeparator(
    QToolBarSeparator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQToolBarSeparator *>(self)->take(key, call);
}
