//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfolderdialogimpl
//  _p_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickDialogs2QuickImpl/qtquickdialogs2quickimplexports.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfolderdialogimpl_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfolderdialogimpl_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qeventpoint.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpalette.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/private/qquickfolderdialogimpl_p.h>
#include <QtQuickDialogs2QuickImpl/private/qquickfolderdialogimpl_p_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtQuickTemplates2/private/qquickdialogbuttonbox_p_p.h>
#include <QtQuickDialogs2QuickImpl/private/qquickfiledialogdelegate_p.h>
#include <QtQuickDialogs2QuickImpl/private/qquickfolderbreadcrumbbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfolderdialogimpl.cpp, line 20, as _ZN29QQuickFolderDialogImplPrivateC1Ev
inline QQuickFolderDialogImplPrivate::QQuickFolderDialogImplPrivate()
{
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfolderdialogimpl.cpp, line 305, as _ZN29QQuickFolderDialogImplPrivate14attachedOrWarnEv
inline QQuickFolderDialogImplAttached *QQuickFolderDialogImplPrivate::attachedOrWarn()
{
    Q_Q(QQuickFolderDialogImpl);
    QQuickFolderDialogImplAttached *attached = static_cast<QQuickFolderDialogImplAttached*>(
        qmlAttachedPropertiesObject<QQuickFolderDialogImpl>(q));
    if (!attached)
        qmlWarning(q) << "Expected FileDialogImpl attached object to be present on" << this;
    return attached;
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfolderdialogimpl.cpp, line 24, as _ZN29QQuickFolderDialogImplPrivate13updateEnabledEv
inline void QQuickFolderDialogImplPrivate::updateEnabled()
{
    Q_Q(QQuickFolderDialogImpl);
    if (!buttonBox)
        return;

    QQuickFolderDialogImplAttached *attached = attachedOrWarn();
    if (!attached)
        return;

    auto openButton = buttonBox->standardButton(QPlatformDialogHelper::Open);
    if (!openButton) {
        qmlWarning(q).nospace() << "Can't update Open button's enabled state because it wasn't found";
        return;
    }

    openButton->setEnabled(!selectedFolder.isEmpty() && attached->breadcrumbBar()
        && !attached->breadcrumbBar()->textField()->isVisible());
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfolderdialogimpl.cpp, line 51, as _ZN29QQuickFolderDialogImplPrivate20updateSelectedFolderERK7QString
inline void QQuickFolderDialogImplPrivate::updateSelectedFolder(const QString &oldFolderPath)
{
    Q_Q(QQuickFolderDialogImpl);
    QQuickFolderDialogImplAttached *attached = attachedOrWarn();
    if (!attached || !attached->folderDialogListView())
        return;

    QString newSelectedFolderPath;
    int newSelectedFolderIndex = 0;
    const QString newFolderPath = QQmlFile::urlToLocalFileOrQrc(currentFolder);
    if (!oldFolderPath.isEmpty() && !newFolderPath.isEmpty()) {
        // If the user went up a directory (or several), we should set
        // selectedFolder to be the directory that we were in (or
        // its closest ancestor that is a child of the new directory).
        // E.g. if oldFolderPath is /foo/bar/baz/abc/xyz, and newFolderPath is /foo/bar,
        // then we want to set selectedFolder to be /foo/bar/baz.
        const int indexOfFolder = oldFolderPath.indexOf(newFolderPath);
        if (indexOfFolder != -1) {
            // [folder]
            // [   oldFolderPath  ]
            // /foo/bar/baz/abc/xyz
            //         [rel...Paths]
            QStringList relativePaths = oldFolderPath.mid(indexOfFolder + newFolderPath.size()).split(QLatin1Char('/'), Qt::SkipEmptyParts);
            newSelectedFolderPath = newFolderPath + QLatin1Char('/') + relativePaths.first();

            // Now find the index of that directory so that we can set the ListView's currentIndex to it.
            const QDir newFolderDir(newFolderPath);
            // Just to be safe...
            if (!newFolderDir.exists()) {
                qmlWarning(q) << "Directory" << newSelectedFolderPath << "doesn't exist; can't get a file entry list for it";
                return;
            }

            const QFileInfoList dirs = newFolderDir.entryInfoList(QDir::Dirs | QDir::NoDotAndDotDot, QDir::DirsFirst);
            const QFileInfo newSelectedFileInfo(newSelectedFolderPath);
            // The directory can contain files, but since we put dirs first, that should never affect the indices.
            newSelectedFolderIndex = dirs.indexOf(newSelectedFileInfo);
        }
    }

    if (newSelectedFolderPath.isEmpty()) {
        // When entering into a directory that isn't a parent of the old one, the first
        // file delegate should be selected.
        // TODO: is there a cheaper way to do this? QDirIterator doesn't support sorting,
        // so we can't use that. QQuickFolderListModel uses threads to fetch its data,
        // so should be considered asynchronous. We might be able to use it, but it would
        // complicate the code even more...
        QDir newFolderDir(newFolderPath);
        if (newFolderDir.exists()) {
            const QFileInfoList files = newFolderDir.entryInfoList(QDir::Dirs | QDir::NoDotAndDotDot, QDir::DirsFirst);
            if (!files.isEmpty())
                newSelectedFolderPath = files.first().absoluteFilePath();
        }
    }

    const bool folderSelected = !newSelectedFolderPath.isEmpty();
    q->setSelectedFolder(folderSelected ? QUrl::fromLocalFile(newSelectedFolderPath) : QUrl());
    {
        // Set the appropriate currentIndex for the selected folder. We block signals from ListView
        // because we don't want folderDialogListViewCurrentIndexChanged to be called, as the file
        // it gets from the delegate will not be up-to-date (but most importantly because we already
        // just set the selected folder).
        QSignalBlocker blocker(attached->folderDialogListView());
        attached->folderDialogListView()->setCurrentIndex(folderSelected ? newSelectedFolderIndex : -1);
    }
    if (folderSelected) {
        if (QQuickItem *currentItem = attached->folderDialogListView()->currentItem())
            currentItem->forceActiveFocus();
    }
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfolderdialogimpl.cpp, line 122, as _ZN29QQuickFolderDialogImplPrivate12handleAcceptEv
inline void QQuickFolderDialogImplPrivate::handleAccept()
{
    // Let handleClick take care of calling accept().
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfolderdialogimpl.cpp, line 127, as _ZN29QQuickFolderDialogImplPrivate11handleClickEP20QQuickAbstractButton
inline void QQuickFolderDialogImplPrivate::handleClick(QQuickAbstractButton *button)
{
    Q_Q(QQuickFolderDialogImpl);
    if (buttonRole(button) == QPlatformDialogHelper::AcceptRole && selectedFolder.isValid()) {
        q->setSelectedFolder(selectedFolder);
        q->accept();
    }
}
//  -----------------------------------------------------------------------

//  A QQuickFolderDialogImplPrivate that Python can take functions over in. Every QQuickFolderDialogImplPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickFolderDialogImplPrivateCall0)(const void *, int *);
typedef void (*CuteQQuickFolderDialogImplPrivateCall1)(const void *, QQuickAbstractButton *, int *);
typedef void (*CuteQQuickFolderDialogImplPrivateCall2)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickFolderDialogImplPrivateCall3)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickFolderDialogImplPrivateCall4)(const void *, QQuickItem *, const QPointF *, int *);
typedef bool (*CuteQQuickFolderDialogImplPrivateCall5)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickFolderDialogImplPrivateCall6)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickFolderDialogImplPrivateCall7)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickFolderDialogImplPrivateCall8)(const void *, const QEventPoint *, int *);
typedef void (*CuteQQuickFolderDialogImplPrivateCall9)(const void *, int *);
typedef int (*CuteQQuickFolderDialogImplPrivateCall10)(const void *, int *);
typedef void (*CuteQQuickFolderDialogImplPrivateCall11)(const void *, int *);
typedef void (*CuteQQuickFolderDialogImplPrivateCall12)(const void *, int *);
typedef void (*CuteQQuickFolderDialogImplPrivateCall13)(const void *, int *);
typedef bool (*CuteQQuickFolderDialogImplPrivateCall14)(const void *, int *);
typedef bool (*CuteQQuickFolderDialogImplPrivateCall15)(const void *, int *);
typedef void (*CuteQQuickFolderDialogImplPrivateCall16)(const void *, int *);
typedef void (*CuteQQuickFolderDialogImplPrivateCall17)(const void *, int *);
typedef void (*CuteQQuickFolderDialogImplPrivateCall18)(const void *, int *);
typedef void * (*CuteQQuickFolderDialogImplPrivateCall19)(const void *, int *);
typedef void (*CuteQQuickFolderDialogImplPrivateCall20)(const void *, QQuickItem *, int *);
typedef const QPalette * (*CuteQQuickFolderDialogImplPrivateCall21)(const void *, int *);
typedef void (*CuteQQuickFolderDialogImplPrivateCall22)(const void *, const QPalette *, int *);
class CuteQQuickFolderDialogImplPrivate : public QQuickFolderDialogImplPrivate {
public:
  using QQuickFolderDialogImplPrivate::QQuickFolderDialogImplPrivate;
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

  //  void QQuickFolderDialogImplPrivate::handleAccept()
  void handleAccept() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickFolderDialogImplPrivateCall0 call = reinterpret_cast<CuteQQuickFolderDialogImplPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickFolderDialogImplPrivate::handleAccept();
  }

  //  void QQuickFolderDialogImplPrivate::handleClick(QQuickAbstractButton
  //      *button)
  void handleClick(QQuickAbstractButton *button) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickFolderDialogImplPrivateCall1 call = reinterpret_cast<CuteQQuickFolderDialogImplPrivateCall1>(taken[1]);
      call(this, button, &handled);
      if (handled) return;
    }
    QQuickFolderDialogImplPrivate::handleClick(button);
  }

  //  void QQuickDialogPrivate::handleReject()
  void handleReject() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickFolderDialogImplPrivateCall2 call = reinterpret_cast<CuteQQuickFolderDialogImplPrivateCall2>(taken[2]);
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
      CuteQQuickFolderDialogImplPrivateCall3 call = reinterpret_cast<CuteQQuickFolderDialogImplPrivateCall3>(taken[3]);
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
      CuteQQuickFolderDialogImplPrivateCall4 call = reinterpret_cast<CuteQQuickFolderDialogImplPrivateCall4>(taken[4]);
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
      CuteQQuickFolderDialogImplPrivateCall5 call = reinterpret_cast<CuteQQuickFolderDialogImplPrivateCall5>(taken[5]);
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
      CuteQQuickFolderDialogImplPrivateCall6 call = reinterpret_cast<CuteQQuickFolderDialogImplPrivateCall6>(taken[6]);
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
      CuteQQuickFolderDialogImplPrivateCall7 call = reinterpret_cast<CuteQQuickFolderDialogImplPrivateCall7>(taken[7]);
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
      CuteQQuickFolderDialogImplPrivateCall8 call = reinterpret_cast<CuteQQuickFolderDialogImplPrivateCall8>(taken[8]);
      bool given = call(this, &a0, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::handleReleaseWithoutGrab(a0);
  }

  //  void QQuickPopupPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickFolderDialogImplPrivateCall9 call = reinterpret_cast<CuteQQuickFolderDialogImplPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::handleUngrab();
  }

  //  QQuickPopup::PopupType QQuickPopupPrivate::resolvedPopupType() const
  QQuickPopup::PopupType resolvedPopupType() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickFolderDialogImplPrivateCall10 call = reinterpret_cast<CuteQQuickFolderDialogImplPrivateCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickPopup::PopupType>(given);
    }
    return QQuickPopupPrivate::resolvedPopupType();
  }

  //  void QQuickPopupPrivate::showDimmer()
  void showDimmer() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickFolderDialogImplPrivateCall11 call = reinterpret_cast<CuteQQuickFolderDialogImplPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::showDimmer();
  }

  //  void QQuickPopupPrivate::hideDimmer()
  void hideDimmer() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickFolderDialogImplPrivateCall12 call = reinterpret_cast<CuteQQuickFolderDialogImplPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::hideDimmer();
  }

  //  void QQuickPopupPrivate::resizeDimmer()
  void resizeDimmer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickFolderDialogImplPrivateCall13 call = reinterpret_cast<CuteQQuickFolderDialogImplPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::resizeDimmer();
  }

  //  bool QQuickPopupPrivate::prepareEnterTransition()
  bool prepareEnterTransition() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickFolderDialogImplPrivateCall14 call = reinterpret_cast<CuteQQuickFolderDialogImplPrivateCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::prepareEnterTransition();
  }

  //  bool QQuickPopupPrivate::prepareExitTransition()
  bool prepareExitTransition() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickFolderDialogImplPrivateCall15 call = reinterpret_cast<CuteQQuickFolderDialogImplPrivateCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::prepareExitTransition();
  }

  //  void QQuickPopupPrivate::finalizeEnterTransition()
  void finalizeEnterTransition() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickFolderDialogImplPrivateCall16 call = reinterpret_cast<CuteQQuickFolderDialogImplPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::finalizeEnterTransition();
  }

  //  void QQuickPopupPrivate::finalizeExitTransition()
  void finalizeExitTransition() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickFolderDialogImplPrivateCall17 call = reinterpret_cast<CuteQQuickFolderDialogImplPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::finalizeExitTransition();
  }

  //  void QQuickPopupPrivate::opened()
  void opened() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickFolderDialogImplPrivateCall18 call = reinterpret_cast<CuteQQuickFolderDialogImplPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::opened();
  }

  //  QQuickPopupPositioner *QQuickPopupPrivate::getPositioner()
  QQuickPopupPositioner *getPositioner() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickFolderDialogImplPrivateCall19 call = reinterpret_cast<CuteQQuickFolderDialogImplPrivateCall19>(taken[19]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickPopupPositioner *>(given);
    }
    return QQuickPopupPrivate::getPositioner();
  }

  //  void QQuickPopupPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickFolderDialogImplPrivateCall20 call = reinterpret_cast<CuteQQuickFolderDialogImplPrivateCall20>(taken[20]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::itemDestroyed(item);
  }

  //  QPalette QQuickPopupPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickFolderDialogImplPrivateCall21 call = reinterpret_cast<CuteQQuickFolderDialogImplPrivateCall21>(taken[21]);
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
      CuteQQuickFolderDialogImplPrivateCall22 call = reinterpret_cast<CuteQQuickFolderDialogImplPrivateCall22>(taken[22]);
      call(this, &parentPalette, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::updateChildrenPalettes(parentPalette);
  }
};

//  QQuickFolderDialogImpl *QQuickFolderDialogImplPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickFolderDialogImpl *ritual_ZN29QQuickFolderDialogImplPrivate6q_funcEv(
    QQuickFolderDialogImplPrivate *self) {
  return self->q_func();
}

//  const QQuickFolderDialogImpl *QQuickFolderDialogImplPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickFolderDialogImpl *ritual_ZNK29QQuickFolderDialogImplPrivate6q_funcEv(
    const QQuickFolderDialogImplPrivate *self) {
  return self->q_func();
}

//  QQuickFolderDialogImplPrivate::QQuickFolderDialogImplPrivate()
extern "C" Q_DECL_EXPORT
QQuickFolderDialogImplPrivate *ritual_ZN29QQuickFolderDialogImplPrivateC1Ev() {
  return new CuteQQuickFolderDialogImplPrivate();
}

//  QQuickFolderDialogImplPrivate
//      *QQuickFolderDialogImplPrivate::get(QQuickFolderDialogImpl *dialog)
extern "C" Q_DECL_EXPORT
QQuickFolderDialogImplPrivate *ritual_ZN29QQuickFolderDialogImplPrivate3getEP22QQuickFolderDialogImpl(
    QQuickFolderDialogImpl *dialog) {
  return QQuickFolderDialogImplPrivate::get(dialog);
}

//  QQuickFolderDialogImplAttached
//      *QQuickFolderDialogImplPrivate::attachedOrWarn()
extern "C" Q_DECL_EXPORT
QQuickFolderDialogImplAttached *ritual_ZN29QQuickFolderDialogImplPrivate14attachedOrWarnEv(
    QQuickFolderDialogImplPrivate *self) {
  return self->attachedOrWarn();
}

//  void QQuickFolderDialogImplPrivate::updateEnabled()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickFolderDialogImplPrivate13updateEnabledEv(
    QQuickFolderDialogImplPrivate *self) {
  self->updateEnabled();
}

//  void QQuickFolderDialogImplPrivate::updateSelectedFolder(const QString
//      &oldFolderPath)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickFolderDialogImplPrivate20updateSelectedFolderERK7QString(
    QQuickFolderDialogImplPrivate *self,
    const QString *oldFolderPath) {
  self->updateSelectedFolder(*oldFolderPath);
}

//  void QQuickFolderDialogImplPrivate::handleAccept()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickFolderDialogImplPrivate12handleAcceptEv(
    QQuickFolderDialogImplPrivate *self) {
  self->handleAccept();
}

//  void QQuickFolderDialogImplPrivate::handleClick(QQuickAbstractButton
//      *button)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickFolderDialogImplPrivate11handleClickEP20QQuickAbstractButton(
    QQuickFolderDialogImplPrivate *self,
    QQuickAbstractButton *button) {
  self->handleClick(button);
}

//  a Python function taken by a CuteQQuickFolderDialogImplPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickFolderDialogImplPrivate(
    QQuickFolderDialogImplPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickFolderDialogImplPrivate *>(self)->take(key, call);
}

//  void QQuickFolderDialogImplPrivate::handleAccept()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QQuickFolderDialogImplPrivate12handleAcceptEv(
    QQuickFolderDialogImplPrivate *self) {
  self->QQuickFolderDialogImplPrivate::handleAccept();
}

//  void QQuickFolderDialogImplPrivate::handleClick(QQuickAbstractButton
//      *button)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QQuickFolderDialogImplPrivate11handleClickEP20QQuickAbstractButton(
    QQuickFolderDialogImplPrivate *self,
    QQuickAbstractButton *button) {
  self->QQuickFolderDialogImplPrivate::handleClick(button);
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
