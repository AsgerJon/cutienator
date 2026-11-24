//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfiledialogimpl_p
//  _p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickDialogs2QuickImpl/qtquickdialogs2quickimplexports.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfiledialogimpl_p.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfiledialogimpl_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qdir.h>
#include <QtCore/qfileinfo.h>
#include <QtGui/qeventpoint.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpalette.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQuickFileDialogImplPrivate that Python can take functions over in. Every QQuickFileDialogImplPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickFileDialogImplPrivateCall0)(const void *, int *);
typedef void (*CuteQQuickFileDialogImplPrivateCall1)(const void *, QQuickAbstractButton *, int *);
typedef void (*CuteQQuickFileDialogImplPrivateCall2)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickFileDialogImplPrivateCall3)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickFileDialogImplPrivateCall4)(const void *, QQuickItem *, const QPointF *, int *);
typedef bool (*CuteQQuickFileDialogImplPrivateCall5)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickFileDialogImplPrivateCall6)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickFileDialogImplPrivateCall7)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickFileDialogImplPrivateCall8)(const void *, const QEventPoint *, int *);
typedef void (*CuteQQuickFileDialogImplPrivateCall9)(const void *, int *);
typedef int (*CuteQQuickFileDialogImplPrivateCall10)(const void *, int *);
typedef void (*CuteQQuickFileDialogImplPrivateCall11)(const void *, int *);
typedef void (*CuteQQuickFileDialogImplPrivateCall12)(const void *, int *);
typedef void (*CuteQQuickFileDialogImplPrivateCall13)(const void *, int *);
typedef bool (*CuteQQuickFileDialogImplPrivateCall14)(const void *, int *);
typedef bool (*CuteQQuickFileDialogImplPrivateCall15)(const void *, int *);
typedef void (*CuteQQuickFileDialogImplPrivateCall16)(const void *, int *);
typedef void (*CuteQQuickFileDialogImplPrivateCall17)(const void *, int *);
typedef void (*CuteQQuickFileDialogImplPrivateCall18)(const void *, int *);
typedef void * (*CuteQQuickFileDialogImplPrivateCall19)(const void *, int *);
typedef void (*CuteQQuickFileDialogImplPrivateCall20)(const void *, QQuickItem *, int *);
typedef const QPalette * (*CuteQQuickFileDialogImplPrivateCall21)(const void *, int *);
typedef void (*CuteQQuickFileDialogImplPrivateCall22)(const void *, const QPalette *, int *);
class CuteQQuickFileDialogImplPrivate : public QQuickFileDialogImplPrivate {
public:
  using QQuickFileDialogImplPrivate::QQuickFileDialogImplPrivate;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QQuickDialogPrivate12handleAcceptEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickDialogPrivate11handleClickEP20QQuickAbstractButton")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickDialogPrivate12handleRejectEv")) {
      taken[2] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate11acceptTouchERK11QEventPoint")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZNK18QQuickPopupPrivate10blockInputEP10QQuickItemRK7QPointF")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate11handlePressEP10QQuickItemRK7QPointFm")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate10handleMoveEP10QQuickItemRK7QPointFm")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate13handleReleaseEP10QQuickItemRK7QPointFm")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate24handleReleaseWithoutGrabERK11QEventPoint")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate12handleUngrabEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QQuickPopupPrivate17resolvedPopupTypeEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate10showDimmerEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate10hideDimmerEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate12resizeDimmerEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate22prepareEnterTransitionEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate21prepareExitTransitionEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate23finalizeEnterTransitionEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate22finalizeExitTransitionEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate6openedEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate13getPositionerEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate13itemDestroyedEP10QQuickItem")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QQuickPopupPrivate14defaultPaletteEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate22updateChildrenPalettesERK8QPalette")) {
      taken[22] = call;
      return true;
    }
    return false;
  }

  //  void QQuickFileDialogImplPrivate::handleAccept()
  void handleAccept() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickFileDialogImplPrivateCall0 call = reinterpret_cast<CuteQQuickFileDialogImplPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickFileDialogImplPrivate::handleAccept();
  }

  //  void QQuickFileDialogImplPrivate::handleClick(QQuickAbstractButton
  //      *button)
  void handleClick(QQuickAbstractButton *button) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickFileDialogImplPrivateCall1 call = reinterpret_cast<CuteQQuickFileDialogImplPrivateCall1>(taken[1]);
      call(this, button, &handled);
      if (handled) return;
    }
    QQuickFileDialogImplPrivate::handleClick(button);
  }

  //  void QQuickDialogPrivate::handleReject()
  void handleReject() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickFileDialogImplPrivateCall2 call = reinterpret_cast<CuteQQuickFileDialogImplPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickDialogPrivate::handleReject();
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  bool QQuickPopupPrivate::acceptTouch(const QTouchEvent::TouchPoint
  //      &point)
  bool acceptTouch(const QTouchEvent::TouchPoint &point) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickFileDialogImplPrivateCall3 call = reinterpret_cast<CuteQQuickFileDialogImplPrivateCall3>(taken[3]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::acceptTouch(point);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

  //  bool QQuickPopupPrivate::blockInput(QQuickItem *item, const QPointF
  //      &point) const
  bool blockInput(QQuickItem *item, const QPointF &point) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickFileDialogImplPrivateCall4 call = reinterpret_cast<CuteQQuickFileDialogImplPrivateCall4>(taken[4]);
      bool given = call(this, item, &point, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::blockInput(item, point);
  }

  //  bool QQuickPopupPrivate::handlePress(QQuickItem *item, const QPointF
  //      &point, ulong timestamp)
  bool handlePress(
      QQuickItem *item,
      const QPointF &point,
      ulong timestamp) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickFileDialogImplPrivateCall5 call = reinterpret_cast<CuteQQuickFileDialogImplPrivateCall5>(taken[5]);
      bool given = call(this, item, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::handlePress(item, point, timestamp);
  }

  //  bool QQuickPopupPrivate::handleMove(QQuickItem *item, const QPointF
  //      &point, ulong timestamp)
  bool handleMove(
      QQuickItem *item,
      const QPointF &point,
      ulong timestamp) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickFileDialogImplPrivateCall6 call = reinterpret_cast<CuteQQuickFileDialogImplPrivateCall6>(taken[6]);
      bool given = call(this, item, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::handleMove(item, point, timestamp);
  }

  //  bool QQuickPopupPrivate::handleRelease(QQuickItem *item, const
  //      QPointF &point, ulong timestamp)
  bool handleRelease(
      QQuickItem *item,
      const QPointF &point,
      ulong timestamp) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickFileDialogImplPrivateCall7 call = reinterpret_cast<CuteQQuickFileDialogImplPrivateCall7>(taken[7]);
      bool given = call(this, item, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::handleRelease(item, point, timestamp);
  }

  //  bool QQuickPopupPrivate::handleReleaseWithoutGrab(const QEventPoint
  //      &a0)
  bool handleReleaseWithoutGrab(const QEventPoint &a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickFileDialogImplPrivateCall8 call = reinterpret_cast<CuteQQuickFileDialogImplPrivateCall8>(taken[8]);
      bool given = call(this, &a0, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::handleReleaseWithoutGrab(a0);
  }

  //  void QQuickPopupPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickFileDialogImplPrivateCall9 call = reinterpret_cast<CuteQQuickFileDialogImplPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::handleUngrab();
  }

  //  QQuickPopup::PopupType QQuickPopupPrivate::resolvedPopupType() const
  QQuickPopup::PopupType resolvedPopupType() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickFileDialogImplPrivateCall10 call = reinterpret_cast<CuteQQuickFileDialogImplPrivateCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickPopup::PopupType>(given);
    }
    return QQuickPopupPrivate::resolvedPopupType();
  }

  //  void QQuickPopupPrivate::showDimmer()
  void showDimmer() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickFileDialogImplPrivateCall11 call = reinterpret_cast<CuteQQuickFileDialogImplPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::showDimmer();
  }

  //  void QQuickPopupPrivate::hideDimmer()
  void hideDimmer() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickFileDialogImplPrivateCall12 call = reinterpret_cast<CuteQQuickFileDialogImplPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::hideDimmer();
  }

  //  void QQuickPopupPrivate::resizeDimmer()
  void resizeDimmer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickFileDialogImplPrivateCall13 call = reinterpret_cast<CuteQQuickFileDialogImplPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::resizeDimmer();
  }

  //  bool QQuickPopupPrivate::prepareEnterTransition()
  bool prepareEnterTransition() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickFileDialogImplPrivateCall14 call = reinterpret_cast<CuteQQuickFileDialogImplPrivateCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::prepareEnterTransition();
  }

  //  bool QQuickPopupPrivate::prepareExitTransition()
  bool prepareExitTransition() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickFileDialogImplPrivateCall15 call = reinterpret_cast<CuteQQuickFileDialogImplPrivateCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::prepareExitTransition();
  }

  //  void QQuickPopupPrivate::finalizeEnterTransition()
  void finalizeEnterTransition() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickFileDialogImplPrivateCall16 call = reinterpret_cast<CuteQQuickFileDialogImplPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::finalizeEnterTransition();
  }

  //  void QQuickPopupPrivate::finalizeExitTransition()
  void finalizeExitTransition() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickFileDialogImplPrivateCall17 call = reinterpret_cast<CuteQQuickFileDialogImplPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::finalizeExitTransition();
  }

  //  void QQuickPopupPrivate::opened()
  void opened() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickFileDialogImplPrivateCall18 call = reinterpret_cast<CuteQQuickFileDialogImplPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::opened();
  }

  //  QQuickPopupPositioner *QQuickPopupPrivate::getPositioner()
  QQuickPopupPositioner *getPositioner() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickFileDialogImplPrivateCall19 call = reinterpret_cast<CuteQQuickFileDialogImplPrivateCall19>(taken[19]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickPopupPositioner *>(given);
    }
    return QQuickPopupPrivate::getPositioner();
  }

  //  void QQuickPopupPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickFileDialogImplPrivateCall20 call = reinterpret_cast<CuteQQuickFileDialogImplPrivateCall20>(taken[20]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::itemDestroyed(item);
  }

  //  QPalette QQuickPopupPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickFileDialogImplPrivateCall21 call = reinterpret_cast<CuteQQuickFileDialogImplPrivateCall21>(taken[21]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickPopupPrivate::defaultPalette();
  }

  //  void QQuickPopupPrivate::updateChildrenPalettes(const QPalette
  //      &parentPalette)
  void updateChildrenPalettes(const QPalette &parentPalette) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickFileDialogImplPrivateCall22 call = reinterpret_cast<CuteQQuickFileDialogImplPrivateCall22>(taken[22]);
      call(this, &parentPalette, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::updateChildrenPalettes(parentPalette);
  }
};

//  QQuickFileDialogImpl *QQuickFileDialogImplPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickFileDialogImpl *ritual_ZN27QQuickFileDialogImplPrivate6q_funcEv(
    QQuickFileDialogImplPrivate *self) {
  return self->q_func();
}

//  const QQuickFileDialogImpl *QQuickFileDialogImplPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickFileDialogImpl *ritual_ZNK27QQuickFileDialogImplPrivate6q_funcEv(
    const QQuickFileDialogImplPrivate *self) {
  return self->q_func();
}

//  QQuickFileDialogImplPrivate::QQuickFileDialogImplPrivate()
extern "C" Q_DECL_EXPORT
QQuickFileDialogImplPrivate *ritual_ZN27QQuickFileDialogImplPrivateC1Ev() {
  return new CuteQQuickFileDialogImplPrivate();
}

//  QQuickFileDialogImplPrivate
//      *QQuickFileDialogImplPrivate::get(QQuickFileDialogImpl *dialog)
extern "C" Q_DECL_EXPORT
QQuickFileDialogImplPrivate *ritual_ZN27QQuickFileDialogImplPrivate3getEP20QQuickFileDialogImpl(
    QQuickFileDialogImpl *dialog) {
  return QQuickFileDialogImplPrivate::get(dialog);
}

//  QQuickFileDialogImplAttached
//      *QQuickFileDialogImplPrivate::attachedOrWarn()
extern "C" Q_DECL_EXPORT
QQuickFileDialogImplAttached *ritual_ZN27QQuickFileDialogImplPrivate14attachedOrWarnEv(
    QQuickFileDialogImplPrivate *self) {
  return self->attachedOrWarn();
}

//  void QQuickFileDialogImplPrivate::setNameFilters(const QStringList
//      &filters)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickFileDialogImplPrivate14setNameFiltersERK5QListI7QStringE(
    QQuickFileDialogImplPrivate *self,
    const QList<QString> *filters) {
  self->setNameFilters(*filters);
}

//  void QQuickFileDialogImplPrivate::updateEnabled()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickFileDialogImplPrivate13updateEnabledEv(
    QQuickFileDialogImplPrivate *self) {
  self->updateEnabled();
}

//  void QQuickFileDialogImplPrivate::updateSelectedFile(const QString
//      &oldFolderPath)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickFileDialogImplPrivate18updateSelectedFileERK7QString(
    QQuickFileDialogImplPrivate *self,
    const QString *oldFolderPath) {
  self->updateSelectedFile(*oldFolderPath);
}

//  void QQuickFileDialogImplPrivate::updateFileNameTextEdit()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickFileDialogImplPrivate22updateFileNameTextEditEv(
    QQuickFileDialogImplPrivate *self) {
  self->updateFileNameTextEdit();
}

//  QDir::SortFlags QQuickFileDialogImplPrivate::fileListSortFlags()
extern "C" Q_DECL_EXPORT
int ritual_ZN27QQuickFileDialogImplPrivate17fileListSortFlagsEv() {
  return static_cast<int>(
      QQuickFileDialogImplPrivate::fileListSortFlags().toInt());
}

//  QFileInfoList QQuickFileDialogImplPrivate::fileList(const QDir &dir)
extern "C" Q_DECL_EXPORT
QList<QFileInfo> *ritual_ZN27QQuickFileDialogImplPrivate8fileListERK4QDir(
    const QDir *dir) {
  return new QList<QFileInfo>(QQuickFileDialogImplPrivate::fileList(*dir));
}

//  void QQuickFileDialogImplPrivate::setFileDialogListViewCurrentIndex(int
//      newCurrentIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickFileDialogImplPrivate33setFileDialogListViewCurrentIndexEi(
    QQuickFileDialogImplPrivate *self,
    int newCurrentIndex) {
  self->setFileDialogListViewCurrentIndex(newCurrentIndex);
}

//  void
//      QQuickFileDialogImplPrivate::tryUpdateFileDialogListViewCurrentIndex(
//      int newCurrentIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickFileDialogImplPrivate39tryUpdateFileDialogListViewCurrentIndexEi(
    QQuickFileDialogImplPrivate *self,
    int newCurrentIndex) {
  self->tryUpdateFileDialogListViewCurrentIndex(newCurrentIndex);
}

//  void QQuickFileDialogImplPrivate::fileDialogListViewCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickFileDialogImplPrivate30fileDialogListViewCountChangedEv(
    QQuickFileDialogImplPrivate *self) {
  self->fileDialogListViewCountChanged();
}

//  void QQuickFileDialogImplPrivate::handleAccept()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickFileDialogImplPrivate12handleAcceptEv(
    QQuickFileDialogImplPrivate *self) {
  self->handleAccept();
}

//  void QQuickFileDialogImplPrivate::handleClick(QQuickAbstractButton
//      *button)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickFileDialogImplPrivate11handleClickEP20QQuickAbstractButton(
    QQuickFileDialogImplPrivate *self,
    QQuickAbstractButton *button) {
  self->handleClick(button);
}

//  void QQuickFileDialogImplPrivate::selectFile()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickFileDialogImplPrivate10selectFileEv(
    QQuickFileDialogImplPrivate *self) {
  self->selectFile();
}

//  a Python function taken by a CuteQQuickFileDialogImplPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickFileDialogImplPrivate(
    QQuickFileDialogImplPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickFileDialogImplPrivate *>(self)->take(key, call);
}

//  void QQuickFileDialogImplPrivate::handleAccept()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickFileDialogImplPrivate12handleAcceptEv(
    QQuickFileDialogImplPrivate *self) {
  self->QQuickFileDialogImplPrivate::handleAccept();
}

//  void QQuickFileDialogImplPrivate::handleClick(QQuickAbstractButton
//      *button)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickFileDialogImplPrivate11handleClickEP20QQuickAbstractButton(
    QQuickFileDialogImplPrivate *self,
    QQuickAbstractButton *button) {
  self->QQuickFileDialogImplPrivate::handleClick(button);
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
