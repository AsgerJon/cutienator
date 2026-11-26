//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/selectsignaldialog_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/selectsignaldialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/private/selectsignaldialog_p.h>
#include <QtDesigner/abstractformeditor.h>
#include <QtDesigner/abstractpromotioninterface.h>
#include <QtDesigner/private/abstractintrospection_p.h>
#include <QtDesigner/private/metadatabase_p.h>
#include <QtDesigner/private/widgetdatabase_p.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qpushbutton.h>
#include <QtGui/qscreen.h>
#include <QtGui/qstandarditemmodel.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtCore/qlist.h>
#include <QtCore/qvariant.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only WITH Qt-GPL-exception-1.0
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qttools/src/designer/src/lib/shared/selectsignaldialog.cpp, line 32, as local:selectsignaldialog.cpp:MethodRole
namespace qdesigner_internal {
enum { MethodRole = Qt::UserRole + 1 };
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/selectsignaldialog.cpp, line 34, as local:selectsignaldialog.cpp:Methods
namespace qdesigner_internal {
using Methods = QList<SelectSignalDialog::Method>;
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/selectsignaldialog.cpp, line 118, as local:selectsignaldialog.cpp:msgNoSignals
namespace qdesigner_internal {
static inline QString msgNoSignals()
{
    return QCoreApplication::translate("QDesignerTaskMenu", "no signals available");
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/selectsignaldialog.cpp, line 63, as _ZNK18qdesigner_internal18SelectSignalDialog15methodFromIndexERK11QModelIndex
namespace qdesigner_internal {
inline SelectSignalDialog::Method SelectSignalDialog::methodFromIndex(const QModelIndex &index) const
{
    if (index.isValid()) {
        const QStandardItem *item = m_model->itemFromIndex(index);
        const QVariant data = item->data(MethodRole);
        if (data.canConvert<Method>())
            return data.value<Method>();
    }
    return Method();
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  A qdesigner_internal::SelectSignalDialog that Python can take functions over in. Every qdesigner_internal::SelectSignalDialog
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(dialog)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall0)(const void *, bool, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef const QSize * (*Cuteqdesigner_internal_SelectSignalDialogCall1)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef const QSize * (*Cuteqdesigner_internal_SelectSignalDialogCall2)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall3)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef int (*Cuteqdesigner_internal_SelectSignalDialogCall4)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall5)(const void *, int, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall6)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall7)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall8)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall9)(const void *, QCloseEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall10)(const void *, QShowEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall11)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(dialog)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall12)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(dialog)
typedef bool (*Cuteqdesigner_internal_SelectSignalDialogCall13)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*Cuteqdesigner_internal_SelectSignalDialogCall14)(const void *, int *);
typedef int (*Cuteqdesigner_internal_SelectSignalDialogCall15)(const void *, int, int *);
typedef bool (*Cuteqdesigner_internal_SelectSignalDialogCall16)(const void *, int *);
typedef void * (*Cuteqdesigner_internal_SelectSignalDialogCall17)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_SelectSignalDialogCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall19)(const void *, QMouseEvent *, int *);
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall20)(const void *, QMouseEvent *, int *);
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall21)(const void *, QMouseEvent *, int *);
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall22)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall23)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall24)(const void *, QKeyEvent *, int *);
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall25)(const void *, QFocusEvent *, int *);
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall26)(const void *, QFocusEvent *, int *);
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall27)(const void *, QEnterEvent *, int *);
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall28)(const void *, QEvent *, int *);
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall29)(const void *, QPaintEvent *, int *);
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall30)(const void *, QMoveEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall31)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall32)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall33)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall34)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall35)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall36)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall37)(const void *, QHideEvent *, int *);
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall38)(const void *, QEvent *, int *);
typedef int (*Cuteqdesigner_internal_SelectSignalDialogCall39)(const void *, int, int *);
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall40)(const void *, QPainter *, int *);
typedef void * (*Cuteqdesigner_internal_SelectSignalDialogCall41)(const void *, QPoint *, int *);
typedef void * (*Cuteqdesigner_internal_SelectSignalDialogCall42)(const void *, int *);
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall43)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*Cuteqdesigner_internal_SelectSignalDialogCall44)(const void *, int, int *);
typedef bool (*Cuteqdesigner_internal_SelectSignalDialogCall45)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall46)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall47)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall48)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall49)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_SelectSignalDialogCall50)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class Cuteqdesigner_internal_SelectSignalDialog : public qdesigner_internal::SelectSignalDialog {
public:
  using qdesigner_internal::SelectSignalDialog::SelectSignalDialog;
  void *taken[51] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog4openEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog4execEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog4doneEi")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog6acceptEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog6rejectEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[17] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[30] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[45] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[49] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[50] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(dialog)
  //  void QDialog::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall0 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall0>(taken[0]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QDialog::setVisible(visible);
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  QSize QDialog::sizeHint() const
  QSize sizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall1 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDialog::sizeHint();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  QSize QDialog::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall2 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDialog::minimumSizeHint();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::open()
  void open() override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall3 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::open();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  int QDialog::exec()
  int exec() override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall4 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QDialog::exec();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::done(int a0)
  void done(int a0) override {
    if (taken[5]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall5 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::done(a0);
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::accept()
  void accept() override {
    if (taken[6]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall6 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::accept();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::reject()
  void reject() override {
    if (taken[7]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall7 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::reject();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall8 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::keyPressEvent(a0);
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall9 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::closeEvent(a0);
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall10 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::showEvent(a0);
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall11 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::resizeEvent(a0);
  }
#endif  // QT_CONFIG(dialog)

#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(dialog)
  //  void QDialog::contextMenuEvent(QContextMenuEvent *a0)
  void contextMenuEvent(QContextMenuEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall12 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::contextMenuEvent(a0);
  }
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_CONTEXTMENU)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(dialog)
  //  bool QDialog::eventFilter(QObject *a0, QEvent *a1)
  bool eventFilter(QObject *a0, QEvent *a1) override {
    if (taken[13]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall13 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall13>(taken[13]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QDialog::eventFilter(a0, a1);
  }
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_QOBJECT)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[14]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall14 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[15]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall15 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall15>(taken[15]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[16]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall16 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[17]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall17 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall17>(taken[17]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall18 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall18>(taken[18]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall19 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall20 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall21 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall22 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall23 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall24 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall25 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall26 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall27 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall28 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall29 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall30 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall31 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall32 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall33 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall34 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall35 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall36 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall37 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall38 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[39]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall39 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall39>(taken[39]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[40]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall40 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall40>(taken[40]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[41]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall41 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall41>(taken[41]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[42]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall42 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall42>(taken[42]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall43 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[44]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall44 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall44>(taken[44]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[45]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall45 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall45>(taken[45]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall46 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall47 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall48 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[49]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall49 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall49>(taken[49]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[50]) {
      int handled = 0;
      Cuteqdesigner_internal_SelectSignalDialogCall50 call = reinterpret_cast<Cuteqdesigner_internal_SelectSignalDialogCall50>(taken[50]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *qdesigner_internal::SelectSignalDialog::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal18SelectSignalDialog10metaObjectEv(
    const qdesigner_internal::SelectSignalDialog *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::SelectSignalDialog::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal18SelectSignalDialog11qt_metacastEPKc(
    qdesigner_internal::SelectSignalDialog *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::SelectSignalDialog::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal18SelectSignalDialog11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::SelectSignalDialog *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  qdesigner_internal::SelectSignalDialog::~SelectSignalDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18SelectSignalDialogD1Ev(
    qdesigner_internal::SelectSignalDialog *self) {
  delete self;
}

//  void qdesigner_internal::SelectSignalDialog::currentChanged(const
//      QModelIndex &a0, const QModelIndex &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18SelectSignalDialog14currentChangedERK11QModelIndexS3_(
    qdesigner_internal::SelectSignalDialog *self,
    const QModelIndex *a0,
    const QModelIndex *a1) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::SelectSignalDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "currentChanged(const QModelIndex &,const QModelIndex &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "currentChanged(const QModelIndex &,const QModelIndex &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(a0)),
      const_cast<void *>(static_cast<const void *>(a1)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::SelectSignalDialog::activated(const QModelIndex
//      &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18SelectSignalDialog9activatedERK11QModelIndex(
    qdesigner_internal::SelectSignalDialog *self,
    const QModelIndex *a0) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::SelectSignalDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "activated(const QModelIndex &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "activated(const QModelIndex &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(a0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  Method qdesigner_internal::SelectSignalDialog::methodFromIndex(const
//      QModelIndex &a0) const
extern "C" Q_DECL_EXPORT
qdesigner_internal::SelectSignalDialog::Method *ritual_ZNK18qdesigner_internal18SelectSignalDialog15methodFromIndexERK11QModelIndex(
    const qdesigner_internal::SelectSignalDialog *self,
    const QModelIndex *a0) {
  return new qdesigner_internal::SelectSignalDialog::Method(
      self->methodFromIndex(
          *a0));
}

//  a Python function taken by a Cuteqdesigner_internal_SelectSignalDialog,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_SelectSignalDialog(
    qdesigner_internal::SelectSignalDialog *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_SelectSignalDialog *>(self)->take(key, call);
}
