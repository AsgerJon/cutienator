//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qfiledialog_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(filedialog)
#if QT_CONFIG(filedialog)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qfiledialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtWidgets/private/qwidgetitemdata_p.h>
#include <QtWidgets/qfiledialog.h>
#include <QtWidgets/private/qfiledialog_p.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qfontmetrics.h>
#include <QtWidgets/qaction.h>
#include <QtWidgets/qactiongroup.h>
#include <QtWidgets/qheaderview.h>
#if QT_CONFIG(shortcut)
#  include <QtWidgets/qshortcut.h>
#endif
#include <QtWidgets/qgridlayout.h>
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#endif
#if QT_CONFIG(messagebox)
#include <QtWidgets/qmessagebox.h>
#endif
#include <stdlib.h>
#if QT_CONFIG(settings)
#include <QtCore/qsettings.h>
#endif
#include <QtCore/qdebug.h>
#if QT_CONFIG(mimetype)
#include <QtCore/qmimedatabase.h>
#endif
#if QT_CONFIG(regularexpression)
#include <QtCore/qregularexpression.h>
#endif
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qstylepainter.h>
#if defined(Q_OS_UNIX)
#include <pwd.h>
#include <unistd.h> // for pathconf() on OS X
#elif defined(Q_OS_WIN)
#  include <QtCore/qt_windows.h>
#endif
#if defined(Q_OS_WASM)
#include <QtGui/private/qwasmlocalfileaccess_p.h>
#endif
#include <algorithm>
#include <QtCore/QMetaEnum>
#if QT_CONFIG(shortcut)
#  include <QtWidgets/qshortcut.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/dialogs/qfiledialog.cpp, line 4116, as _ZN19QFileDialogListView20setFileDialogPrivateEP18QFileDialogPrivate
inline void QFileDialogListView::setFileDialogPrivate(QFileDialogPrivate *d_pointer)
{
    d_ptr = d_pointer;
    setSelectionBehavior(QAbstractItemView::SelectRows);
    setWrapping(true);
    setResizeMode(QListView::Adjust);
    setEditTriggers(QAbstractItemView::EditKeyPressed);
    setContextMenuPolicy(Qt::CustomContextMenu);
#if QT_CONFIG(draganddrop)
    setDragDropMode(QAbstractItemView::InternalMove);
#endif
}

//  from src/widgets/dialogs/qfiledialog.cpp, line 4129, as _ZNK19QFileDialogListView8sizeHintEv
inline QSize QFileDialogListView::sizeHint() const
{
    int height = qMax(10, sizeHintForRow(0));
    return QSize(QListView::sizeHint().width() * 2, height * 30);
}

//  from src/widgets/dialogs/qfiledialog.cpp, line 4135, as _ZN19QFileDialogListView13keyPressEventEP9QKeyEvent
inline void QFileDialogListView::keyPressEvent(QKeyEvent *e)
{
    if (!d_ptr->itemViewKeyboardEvent(e))
        QListView::keyPressEvent(e);
    e->accept();
}
//  -----------------------------------------------------------------------

//  Only a class built on QFileDialogListView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQFileDialogListView : QFileDialogListView {
  using QFileDialogListView::keyPressEvent;
};

//  QFileDialogListView::QFileDialogListView(QWidget *parent)
extern "C" Q_DECL_EXPORT
QFileDialogListView *ritual_ZN19QFileDialogListViewC1EP7QWidget(
    QWidget *parent) {
  return new QFileDialogListView(parent);
}

//  void QFileDialogListView::setFileDialogPrivate(QFileDialogPrivate
//      *d_pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QFileDialogListView20setFileDialogPrivateEP18QFileDialogPrivate(
    QFileDialogListView *self,
    QFileDialogPrivate *d_pointer) {
  self->setFileDialogPrivate(d_pointer);
}

//  QSize QFileDialogListView::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QFileDialogListView8sizeHintEv(
    const QFileDialogListView *self) {
  return new QSize(self->sizeHint());
}

//  void QFileDialogListView::keyPressEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QFileDialogListView13keyPressEventEP9QKeyEvent(
    QFileDialogListView *self,
    QKeyEvent *e) {
  self->keyPressEvent(e);
}

//  QSize QFileDialogListView::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK19QFileDialogListView8sizeHintEv(
    const QFileDialogListView *self) {
  return new QSize(self->QFileDialogListView::sizeHint());
}

//  void QFileDialogListView::keyPressEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QFileDialogListView13keyPressEventEP9QKeyEvent(
    QFileDialogListView *self,
    QKeyEvent *e) {
  static_cast<OwnQFileDialogListView *>(self)->OwnQFileDialogListView::keyPressEvent(
      e);
}

#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(filedialog)
