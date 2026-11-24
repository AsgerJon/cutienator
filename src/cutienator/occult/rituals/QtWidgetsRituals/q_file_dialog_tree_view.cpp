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

//  from src/widgets/dialogs/qfiledialog.cpp, line 4142, as _ZN19QFileDialogTreeView20setFileDialogPrivateEP18QFileDialogPrivate
inline void QFileDialogTreeView::setFileDialogPrivate(QFileDialogPrivate *d_pointer)
{
    d_ptr = d_pointer;
    setSelectionBehavior(QAbstractItemView::SelectRows);
    setRootIsDecorated(false);
    setItemsExpandable(false);
    setSortingEnabled(true);
    header()->setSortIndicator(0, Qt::AscendingOrder);
    header()->setStretchLastSection(false);
    setTextElideMode(Qt::ElideMiddle);
    setEditTriggers(QAbstractItemView::EditKeyPressed);
    setContextMenuPolicy(Qt::CustomContextMenu);
#if QT_CONFIG(draganddrop)
    setDragDropMode(QAbstractItemView::InternalMove);
#endif
}

//  from src/widgets/dialogs/qfiledialog.cpp, line 4166, as _ZNK19QFileDialogTreeView8sizeHintEv
inline QSize QFileDialogTreeView::sizeHint() const
{
    int height = qMax(10, sizeHintForRow(0));
    QSize sizeHint = header()->sizeHint();
    return QSize(sizeHint.width() * 4, height * 30);
}

//  from src/widgets/dialogs/qfiledialog.cpp, line 4159, as _ZN19QFileDialogTreeView13keyPressEventEP9QKeyEvent
inline void QFileDialogTreeView::keyPressEvent(QKeyEvent *e)
{
    if (!d_ptr->itemViewKeyboardEvent(e))
        QTreeView::keyPressEvent(e);
    e->accept();
}
//  -----------------------------------------------------------------------

//  Only a class built on QFileDialogTreeView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQFileDialogTreeView : QFileDialogTreeView {
  using QFileDialogTreeView::keyPressEvent;
};

//  QFileDialogTreeView::QFileDialogTreeView(QWidget *parent)
extern "C" Q_DECL_EXPORT
QFileDialogTreeView *ritual_ZN19QFileDialogTreeViewC1EP7QWidget(
    QWidget *parent) {
  return new QFileDialogTreeView(parent);
}

//  void QFileDialogTreeView::setFileDialogPrivate(QFileDialogPrivate
//      *d_pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QFileDialogTreeView20setFileDialogPrivateEP18QFileDialogPrivate(
    QFileDialogTreeView *self,
    QFileDialogPrivate *d_pointer) {
  self->setFileDialogPrivate(d_pointer);
}

//  QSize QFileDialogTreeView::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QFileDialogTreeView8sizeHintEv(
    const QFileDialogTreeView *self) {
  return new QSize(self->sizeHint());
}

//  void QFileDialogTreeView::keyPressEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QFileDialogTreeView13keyPressEventEP9QKeyEvent(
    QFileDialogTreeView *self,
    QKeyEvent *e) {
  self->keyPressEvent(e);
}

//  QSize QFileDialogTreeView::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK19QFileDialogTreeView8sizeHintEv(
    const QFileDialogTreeView *self) {
  return new QSize(self->QFileDialogTreeView::sizeHint());
}

//  void QFileDialogTreeView::keyPressEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QFileDialogTreeView13keyPressEventEP9QKeyEvent(
    QFileDialogTreeView *self,
    QKeyEvent *e) {
  static_cast<OwnQFileDialogTreeView *>(self)->OwnQFileDialogTreeView::keyPressEvent(
      e);
}

#endif  // QT_CONFIG(filedialog)
