//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qfiledialog_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(filedialog)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qfiledialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <qvariant.h>
#include <private/qwidgetitemdata_p.h>
#include "qfiledialog.h"
#include "qfiledialog_p.h"
#include <private/qapplication_p.h>
#include <private/qguiapplication_p.h>
#include <qfontmetrics.h>
#include <qaction.h>
#include <qactiongroup.h>
#include <qheaderview.h>
#if QT_CONFIG(shortcut)
#  include <qshortcut.h>
#endif
#include <qgridlayout.h>
#if QT_CONFIG(menu)
#include <qmenu.h>
#endif
#if QT_CONFIG(messagebox)
#include <qmessagebox.h>
#endif
#include <stdlib.h>
#if QT_CONFIG(settings)
#include <qsettings.h>
#endif
#include <qdebug.h>
#if QT_CONFIG(mimetype)
#include <qmimedatabase.h>
#endif
#if QT_CONFIG(regularexpression)
#include <qregularexpression.h>
#endif
#include <qapplication.h>
#include <qstylepainter.h>
#if defined(Q_OS_UNIX)
#include <pwd.h>
#include <unistd.h> // for pathconf() on OS X
#elif defined(Q_OS_WIN)
#  include <QtCore/qt_windows.h>
#endif
#if defined(Q_OS_WASM)
#include <private/qwasmlocalfileaccess_p.h>
#endif
#include <algorithm>
#include <QMetaEnum>
#if QT_CONFIG(shortcut)
#  include <qshortcut.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/dialogs/qfiledialog.cpp, line 4183, as _ZN19QFileDialogLineEdit13keyPressEventEP9QKeyEvent
inline void QFileDialogLineEdit::keyPressEvent(QKeyEvent *e)
{
#if QT_CONFIG(shortcut)
    int key = e->key();
#endif
    QLineEdit::keyPressEvent(e);
#if QT_CONFIG(shortcut)
    if (!e->matches(QKeySequence::Cancel) && key != Qt::Key_Back)
#endif
        e->accept();
}
//  -----------------------------------------------------------------------

//  A QFileDialogLineEdit that Python can take functions over in. Every QFileDialogLineEdit
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(filedialog)
typedef void (*CuteQFileDialogLineEditCall0)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(filedialog)
#if QT_CONFIG(lineedit)
typedef const QSize * (*CuteQFileDialogLineEditCall1)(const void *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef const QSize * (*CuteQFileDialogLineEditCall2)(const void *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*CuteQFileDialogLineEditCall3)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*CuteQFileDialogLineEditCall4)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*CuteQFileDialogLineEditCall5)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*CuteQFileDialogLineEditCall6)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*CuteQFileDialogLineEditCall7)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*CuteQFileDialogLineEditCall8)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*CuteQFileDialogLineEditCall9)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*CuteQFileDialogLineEditCall10)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
typedef void (*CuteQFileDialogLineEditCall11)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
typedef void (*CuteQFileDialogLineEditCall12)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
typedef void (*CuteQFileDialogLineEditCall13)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
typedef void (*CuteQFileDialogLineEditCall14)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(lineedit)
typedef void (*CuteQFileDialogLineEditCall15)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(lineedit)
typedef void (*CuteQFileDialogLineEditCall16)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(lineedit)
typedef void (*CuteQFileDialogLineEditCall17)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef void (*CuteQFileDialogLineEditCall18)(const void *, QStyleOptionFrame *, int *);
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
typedef const QVariant * (*CuteQFileDialogLineEditCall19)(const void *, int, int *);
#endif  // QT_CONFIG(lineedit)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(lineedit)
typedef void (*CuteQFileDialogLineEditCall20)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(lineedit)
typedef bool (*CuteQFileDialogLineEditCall21)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteQFileDialogLineEditCall22)(const void *, int *);
typedef void (*CuteQFileDialogLineEditCall23)(const void *, bool, int *);
typedef int (*CuteQFileDialogLineEditCall24)(const void *, int, int *);
typedef bool (*CuteQFileDialogLineEditCall25)(const void *, int *);
typedef void * (*CuteQFileDialogLineEditCall26)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQFileDialogLineEditCall27)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQFileDialogLineEditCall28)(const void *, QEnterEvent *, int *);
typedef void (*CuteQFileDialogLineEditCall29)(const void *, QEvent *, int *);
typedef void (*CuteQFileDialogLineEditCall30)(const void *, QMoveEvent *, int *);
typedef void (*CuteQFileDialogLineEditCall31)(const void *, QResizeEvent *, int *);
typedef void (*CuteQFileDialogLineEditCall32)(const void *, QCloseEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQFileDialogLineEditCall33)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQFileDialogLineEditCall34)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
typedef void (*CuteQFileDialogLineEditCall35)(const void *, QShowEvent *, int *);
typedef void (*CuteQFileDialogLineEditCall36)(const void *, QHideEvent *, int *);
typedef int (*CuteQFileDialogLineEditCall37)(const void *, int, int *);
typedef void (*CuteQFileDialogLineEditCall38)(const void *, QPainter *, int *);
typedef void * (*CuteQFileDialogLineEditCall39)(const void *, QPoint *, int *);
typedef void * (*CuteQFileDialogLineEditCall40)(const void *, int *);
typedef bool (*CuteQFileDialogLineEditCall41)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQFileDialogLineEditCall42)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileDialogLineEditCall43)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileDialogLineEditCall44)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileDialogLineEditCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileDialogLineEditCall46)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQFileDialogLineEdit : public QFileDialogLineEdit {
public:
  using QFileDialogLineEdit::QFileDialogLineEdit;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(filedialog)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(filedialog)
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
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
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

#if QT_CONFIG(filedialog)
  //  void QFileDialogLineEdit::keyPressEvent(QKeyEvent *e)
  void keyPressEvent(QKeyEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQFileDialogLineEditCall0 call = reinterpret_cast<CuteQFileDialogLineEditCall0>(taken[0]);
      call(this, e, &handled);
      if (handled) return;
    }
    QFileDialogLineEdit::keyPressEvent(e);
  }
#endif  // QT_CONFIG(filedialog)

#if QT_CONFIG(lineedit)
  //  QSize QLineEdit::sizeHint() const
  QSize sizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQFileDialogLineEditCall1 call = reinterpret_cast<CuteQFileDialogLineEditCall1>(taken[1]);
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
      CuteQFileDialogLineEditCall2 call = reinterpret_cast<CuteQFileDialogLineEditCall2>(taken[2]);
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
      CuteQFileDialogLineEditCall3 call = reinterpret_cast<CuteQFileDialogLineEditCall3>(taken[3]);
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
      CuteQFileDialogLineEditCall4 call = reinterpret_cast<CuteQFileDialogLineEditCall4>(taken[4]);
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
      CuteQFileDialogLineEditCall5 call = reinterpret_cast<CuteQFileDialogLineEditCall5>(taken[5]);
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
      CuteQFileDialogLineEditCall6 call = reinterpret_cast<CuteQFileDialogLineEditCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::mouseDoubleClickEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQFileDialogLineEditCall7 call = reinterpret_cast<CuteQFileDialogLineEditCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::keyReleaseEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQFileDialogLineEditCall8 call = reinterpret_cast<CuteQFileDialogLineEditCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::focusInEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQFileDialogLineEditCall9 call = reinterpret_cast<CuteQFileDialogLineEditCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLineEdit::focusOutEvent(a0);
  }
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
  //  void QLineEdit::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQFileDialogLineEditCall10 call = reinterpret_cast<CuteQFileDialogLineEditCall10>(taken[10]);
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
      CuteQFileDialogLineEditCall11 call = reinterpret_cast<CuteQFileDialogLineEditCall11>(taken[11]);
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
      CuteQFileDialogLineEditCall12 call = reinterpret_cast<CuteQFileDialogLineEditCall12>(taken[12]);
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
      CuteQFileDialogLineEditCall13 call = reinterpret_cast<CuteQFileDialogLineEditCall13>(taken[13]);
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
      CuteQFileDialogLineEditCall14 call = reinterpret_cast<CuteQFileDialogLineEditCall14>(taken[14]);
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
      CuteQFileDialogLineEditCall15 call = reinterpret_cast<CuteQFileDialogLineEditCall15>(taken[15]);
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
      CuteQFileDialogLineEditCall16 call = reinterpret_cast<CuteQFileDialogLineEditCall16>(taken[16]);
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
      CuteQFileDialogLineEditCall17 call = reinterpret_cast<CuteQFileDialogLineEditCall17>(taken[17]);
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
      CuteQFileDialogLineEditCall18 call = reinterpret_cast<CuteQFileDialogLineEditCall18>(taken[18]);
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
      CuteQFileDialogLineEditCall19 call = reinterpret_cast<CuteQFileDialogLineEditCall19>(taken[19]);
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
      CuteQFileDialogLineEditCall20 call = reinterpret_cast<CuteQFileDialogLineEditCall20>(taken[20]);
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
      CuteQFileDialogLineEditCall21 call = reinterpret_cast<CuteQFileDialogLineEditCall21>(taken[21]);
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
      CuteQFileDialogLineEditCall22 call = reinterpret_cast<CuteQFileDialogLineEditCall22>(taken[22]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[23]) {
      int handled = 0;
      CuteQFileDialogLineEditCall23 call = reinterpret_cast<CuteQFileDialogLineEditCall23>(taken[23]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQFileDialogLineEditCall24 call = reinterpret_cast<CuteQFileDialogLineEditCall24>(taken[24]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQFileDialogLineEditCall25 call = reinterpret_cast<CuteQFileDialogLineEditCall25>(taken[25]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQFileDialogLineEditCall26 call = reinterpret_cast<CuteQFileDialogLineEditCall26>(taken[26]);
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
      CuteQFileDialogLineEditCall27 call = reinterpret_cast<CuteQFileDialogLineEditCall27>(taken[27]);
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
      CuteQFileDialogLineEditCall28 call = reinterpret_cast<CuteQFileDialogLineEditCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQFileDialogLineEditCall29 call = reinterpret_cast<CuteQFileDialogLineEditCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQFileDialogLineEditCall30 call = reinterpret_cast<CuteQFileDialogLineEditCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQFileDialogLineEditCall31 call = reinterpret_cast<CuteQFileDialogLineEditCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQFileDialogLineEditCall32 call = reinterpret_cast<CuteQFileDialogLineEditCall32>(taken[32]);
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
      CuteQFileDialogLineEditCall33 call = reinterpret_cast<CuteQFileDialogLineEditCall33>(taken[33]);
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
      CuteQFileDialogLineEditCall34 call = reinterpret_cast<CuteQFileDialogLineEditCall34>(taken[34]);
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
      CuteQFileDialogLineEditCall35 call = reinterpret_cast<CuteQFileDialogLineEditCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQFileDialogLineEditCall36 call = reinterpret_cast<CuteQFileDialogLineEditCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQFileDialogLineEditCall37 call = reinterpret_cast<CuteQFileDialogLineEditCall37>(taken[37]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQFileDialogLineEditCall38 call = reinterpret_cast<CuteQFileDialogLineEditCall38>(taken[38]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQFileDialogLineEditCall39 call = reinterpret_cast<CuteQFileDialogLineEditCall39>(taken[39]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[40]) {
      int handled = 0;
      CuteQFileDialogLineEditCall40 call = reinterpret_cast<CuteQFileDialogLineEditCall40>(taken[40]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[41]) {
      int handled = 0;
      CuteQFileDialogLineEditCall41 call = reinterpret_cast<CuteQFileDialogLineEditCall41>(taken[41]);
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
      CuteQFileDialogLineEditCall42 call = reinterpret_cast<CuteQFileDialogLineEditCall42>(taken[42]);
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
      CuteQFileDialogLineEditCall43 call = reinterpret_cast<CuteQFileDialogLineEditCall43>(taken[43]);
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
      CuteQFileDialogLineEditCall44 call = reinterpret_cast<CuteQFileDialogLineEditCall44>(taken[44]);
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
      CuteQFileDialogLineEditCall45 call = reinterpret_cast<CuteQFileDialogLineEditCall45>(taken[45]);
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
      CuteQFileDialogLineEditCall46 call = reinterpret_cast<CuteQFileDialogLineEditCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QFileDialogLineEdit::QFileDialogLineEdit(QWidget *parent)
extern "C" Q_DECL_EXPORT
QFileDialogLineEdit *ritual_ZN19QFileDialogLineEditC1EP7QWidget(
    QWidget *parent) {
  return new CuteQFileDialogLineEdit(parent);
}

//  void QFileDialogLineEdit::keyPressEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QFileDialogLineEdit13keyPressEventEP9QKeyEvent(
    QFileDialogLineEdit *self,
    QKeyEvent *e) {
  self->keyPressEvent(e);
}

//  a Python function taken by a CuteQFileDialogLineEdit, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFileDialogLineEdit(
    QFileDialogLineEdit *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFileDialogLineEdit *>(self)->take(key, call);
}

//  void QFileDialogLineEdit::keyPressEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QFileDialogLineEdit13keyPressEventEP9QKeyEvent(
    QFileDialogLineEdit *self,
    QKeyEvent *e) {
  self->QFileDialogLineEdit::keyPressEvent(e);
}

#endif  // QT_CONFIG(filedialog)
