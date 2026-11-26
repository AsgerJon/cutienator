//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/actionrepository_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/actionrepository_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/private/actionrepository_p.h>
#include <QtDesigner/private/qtresourceview_p.h>
#include <QtDesigner/private/iconloader_p.h>
#include <QtDesigner/private/qdesigner_utils_p.h>
#include <QtDesigner/abstractformeditor.h>
#include <QtDesigner/propertysheet.h>
#include <QtDesigner/qextensionmanager.h>
#include <QtWidgets/qtoolbutton.h>
#include <QtWidgets/qheaderview.h>
#include <QtWidgets/qtoolbar.h>
#include <QtWidgets/qmenu.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qaction.h>
#include <QtGui/qdrag.h>
#include <QtGui/qevent.h>
#include <QtGui/qstandarditemmodel.h>
#include <QtCore/qset.h>
#include <QtCore/qdebug.h>
#include <QtCore/qmetaobject.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only WITH Qt-GPL-exception-1.0
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qttools/src/designer/src/lib/shared/actionrepository.cpp, line 34, as local:actionrepository.cpp:listModeIconSize
namespace {
enum { listModeIconSize = 16, iconModeIconSize = 24 };
}  // namespace

//  from ../qttools/src/designer/src/lib/shared/actionrepository.cpp, line 274, as local:actionrepository.cpp:handleImageDragEnterMoveEvent
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
static bool handleImageDragEnterMoveEvent(QDropEvent *event)
{
    QtResourceView::ResourceType type;
    const bool rc = QtResourceView::decodeMimeData(event->mimeData(), &type) && type ==  QtResourceView::ResourceImage;
    if (rc)
        event->acceptProposedAction();
    else
        event->ignore();
    return rc;
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/actionrepository.cpp, line 285, as local:actionrepository.cpp:handleImageDropEvent
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
static void handleImageDropEvent(const QAbstractItemView *iv, QDropEvent *event, ActionModel *am)
{
    const QModelIndex index = iv->indexAt(event->position().toPoint());
    if (!index.isValid()) {
        event->ignore();
        return;
    }

    if (!handleImageDragEnterMoveEvent(event))
        return;

    am->dropMimeData(event->mimeData(),  event->proposedAction(), index.row(), 0, iv->rootIndex());
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/actionrepository.cpp, line 302, as local:actionrepository.cpp:startActionDrag
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void startActionDrag(QWidget *dragParent, ActionModel *model, const QModelIndexList &indexes, Qt::DropActions supportedActions)
{
    if (indexes.isEmpty())
        return;

    QDrag *drag = new QDrag(dragParent);
    QMimeData *data = model->mimeData(indexes);
    drag->setMimeData(data);
    if (ActionRepositoryMimeData *actionMimeData = qobject_cast<ActionRepositoryMimeData *>(data))
        drag->setPixmap(ActionRepositoryMimeData::actionDragPixmap(actionMimeData->actionList().constFirst()));

    drag->exec(supportedActions);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/actionrepository.cpp, line 386, as _ZN18qdesigner_internal14ActionTreeView13slotActivatedERK11QModelIndex
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void ActionTreeView::slotActivated(const QModelIndex &index)
{
    emit actionActivated(m_model->actionAt(index), index.column());
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/actionrepository.cpp, line 380, as _ZN18qdesigner_internal14ActionTreeView14currentChangedERK11QModelIndexS3_
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void ActionTreeView::currentChanged(const QModelIndex &current, const QModelIndex &previous)
{
    emit currentActionChanged(m_model->actionAt(current));
    QTreeView::currentChanged(current, previous);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/actionrepository.cpp, line 352, as _ZN18qdesigner_internal14ActionTreeView14dragEnterEventEP15QDragEnterEvent
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void ActionTreeView::dragEnterEvent(QDragEnterEvent *event)
{
    handleImageDragEnterMoveEvent(event);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/actionrepository.cpp, line 362, as _ZN18qdesigner_internal14ActionTreeView9dropEventEP10QDropEvent
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void ActionTreeView::dropEvent(QDropEvent *event)
{
    handleImageDropEvent(this, event, m_model);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/actionrepository.cpp, line 367, as _ZN18qdesigner_internal14ActionTreeView12focusInEventEP11QFocusEvent
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void ActionTreeView::focusInEvent(QFocusEvent *event)
{
    QTreeView::focusInEvent(event);
    // Make property editor display current action
    if (QAction *a = currentAction())
       emit currentActionChanged(a);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/actionrepository.cpp, line 375, as _ZN18qdesigner_internal14ActionTreeView16contextMenuEventEP17QContextMenuEvent
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void ActionTreeView::contextMenuEvent(QContextMenuEvent *event)
{
    emit actionContextMenuRequested(event, m_model->actionAt(indexAt(event->pos())));
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/actionrepository.cpp, line 391, as _ZN18qdesigner_internal14ActionTreeView9startDragE6QFlagsIN2Qt10DropActionEE
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void ActionTreeView::startDrag(Qt::DropActions supportedActions)
{
    startActionDrag(this, m_model, selectedIndexes(), supportedActions);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/actionrepository.cpp, line 338, as _ZNK18qdesigner_internal14ActionTreeView13currentActionEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline QAction *ActionTreeView::currentAction() const
{
    return m_model->actionAt(currentIndex());
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  Only a class built on qdesigner_internal::ActionTreeView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct Ownqdesigner_internal_ActionTreeView : qdesigner_internal::ActionTreeView {
  using qdesigner_internal::ActionTreeView::dragEnterEvent;
  using qdesigner_internal::ActionTreeView::dropEvent;
  using qdesigner_internal::ActionTreeView::startDrag;
};

//  const QMetaObject *qdesigner_internal::ActionTreeView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal14ActionTreeView10metaObjectEv(
    const qdesigner_internal::ActionTreeView *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::ActionTreeView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal14ActionTreeView11qt_metacastEPKc(
    qdesigner_internal::ActionTreeView *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::ActionTreeView::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal14ActionTreeView11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::ActionTreeView *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QAction *qdesigner_internal::ActionTreeView::currentAction() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK18qdesigner_internal14ActionTreeView13currentActionEv(
    const qdesigner_internal::ActionTreeView *self) {
  return self->currentAction();
}

//  void qdesigner_internal::ActionTreeView::filter(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14ActionTreeView6filterERK7QString(
    qdesigner_internal::ActionTreeView *self,
    const QString *text) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::ActionTreeView")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "filter(const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "filter(const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(text)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::ActionTreeView::actionContextMenuRequested(QCont
//      extMenuEvent *event, QAction *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14ActionTreeView26actionContextMenuRequestedEP17QContextMenuEventP7QAction(
    qdesigner_internal::ActionTreeView *self,
    QContextMenuEvent *event,
    QAction *a1) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::ActionTreeView")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "actionContextMenuRequested(QContextMenuEvent *,QAction *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "actionContextMenuRequested(QContextMenuEvent *,QAction *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&event)),
      const_cast<void *>(static_cast<const void *>(&a1)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::ActionTreeView::currentActionChanged(QAction
//      *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14ActionTreeView20currentActionChangedEP7QAction(
    qdesigner_internal::ActionTreeView *self,
    QAction *action) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::ActionTreeView")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "currentActionChanged(QAction *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "currentActionChanged(QAction *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&action)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::ActionTreeView::actionActivated(QAction *action,
//      int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14ActionTreeView15actionActivatedEP7QActioni(
    qdesigner_internal::ActionTreeView *self,
    QAction *action,
    int column) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::ActionTreeView")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "actionActivated(QAction *,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "actionActivated(QAction *,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&action)),
      const_cast<void *>(static_cast<const void *>(&column)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::ActionTreeView::currentChanged(const QModelIndex
//      &current, const QModelIndex &previous)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14ActionTreeView14currentChangedERK11QModelIndexS3_(
    qdesigner_internal::ActionTreeView *self,
    const QModelIndex *current,
    const QModelIndex *previous) {
  self->currentChanged(*current, *previous);
}

//  void qdesigner_internal::ActionTreeView::dragEnterEvent(QDragEnterEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14ActionTreeView14dragEnterEventEP15QDragEnterEvent(
    qdesigner_internal::ActionTreeView *self,
    QDragEnterEvent *event) {
  self->dragEnterEvent(event);
}

//  void qdesigner_internal::ActionTreeView::dragMoveEvent(QDragMoveEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14ActionTreeView13dragMoveEventEP14QDragMoveEvent(
    qdesigner_internal::ActionTreeView *self,
    QDragMoveEvent *event) {
  self->dragMoveEvent(event);
}

//  void qdesigner_internal::ActionTreeView::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14ActionTreeView9dropEventEP10QDropEvent(
    qdesigner_internal::ActionTreeView *self,
    QDropEvent *event) {
  self->dropEvent(event);
}

//  void qdesigner_internal::ActionTreeView::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14ActionTreeView12focusInEventEP11QFocusEvent(
    qdesigner_internal::ActionTreeView *self,
    QFocusEvent *event) {
  self->focusInEvent(event);
}

//  void
//      qdesigner_internal::ActionTreeView::contextMenuEvent(QContextMenuEven
//      t *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14ActionTreeView16contextMenuEventEP17QContextMenuEvent(
    qdesigner_internal::ActionTreeView *self,
    QContextMenuEvent *event) {
  self->contextMenuEvent(event);
}

//  void qdesigner_internal::ActionTreeView::startDrag(Qt::DropActions
//      supportedActions)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14ActionTreeView9startDragE6QFlagsIN2Qt10DropActionEE(
    qdesigner_internal::ActionTreeView *self,
    int supportedActions) {
  self->startDrag(QFlags<Qt::DropAction>::fromInt(supportedActions));
}

//  void qdesigner_internal::ActionTreeView::slotActivated(const QModelIndex
//      &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14ActionTreeView13slotActivatedERK11QModelIndex(
    qdesigner_internal::ActionTreeView *self,
    const QModelIndex *a0) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::ActionTreeView")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "slotActivated(const QModelIndex &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "slotActivated(const QModelIndex &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(a0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::ActionTreeView::dragEnterEvent(QDragEnterEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14ActionTreeView14dragEnterEventEP15QDragEnterEvent(
    qdesigner_internal::ActionTreeView *self,
    QDragEnterEvent *event) {
  static_cast<Ownqdesigner_internal_ActionTreeView *>(self)->Ownqdesigner_internal_ActionTreeView::dragEnterEvent(
      event);
}

//  void qdesigner_internal::ActionTreeView::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14ActionTreeView9dropEventEP10QDropEvent(
    qdesigner_internal::ActionTreeView *self,
    QDropEvent *event) {
  static_cast<Ownqdesigner_internal_ActionTreeView *>(self)->Ownqdesigner_internal_ActionTreeView::dropEvent(
      event);
}

//  void qdesigner_internal::ActionTreeView::startDrag(Qt::DropActions
//      supportedActions)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14ActionTreeView9startDragE6QFlagsIN2Qt10DropActionEE(
    qdesigner_internal::ActionTreeView *self,
    int supportedActions) {
  static_cast<Ownqdesigner_internal_ActionTreeView *>(self)->Ownqdesigner_internal_ActionTreeView::startDrag(
      QFlags<Qt::DropAction>::fromInt(supportedActions));
}
