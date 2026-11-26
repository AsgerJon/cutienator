//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcompleter_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(completer)
#if QT_CONFIG(completer)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qcompleter.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qcompleter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qitemselectionmodel.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qcompleter_p.h>
#include "QtWidgets/qscrollbar.h"
#include "QtCore/qdir.h"
#if QT_CONFIG(stringlistmodel)
#include "QtCore/qstringlistmodel.h"
#endif
#if QT_CONFIG(filesystemmodel)
#include "QtGui/qfilesystemmodel.h"
#endif
#include "QtWidgets/qheaderview.h"
#if QT_CONFIG(listview)
#include "QtWidgets/qlistview.h"
#endif
#include "QtWidgets/qapplication.h"
#include "QtGui/qevent.h"
#include <QtWidgets/private/qapplication_p.h>
#include <QtWidgets/private/qwidget_p.h>
#include <QtGui/qpa/qplatformwindow.h>
#include <QtGui/qpa/qplatformwindow_p.h>
#if QT_CONFIG(lineedit)
#include "QtWidgets/qlineedit.h"
#endif
#include "QtCore/qdir.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/util/qcompleter.cpp, line 136, as _ZN16QCompletionModelC1EP17QCompleterPrivateP7QObject
inline QCompletionModel::QCompletionModel(QCompleterPrivate *c, QObject *parent)
    : QAbstractProxyModel(*new QCompletionModelPrivate, parent),
      c(c), showAll(false)
{
    createEngine();
}

//  from src/widgets/util/qcompleter.cpp, line 173, as _ZN16QCompletionModel12createEngineEv
inline void QCompletionModel::createEngine()
{
    bool sortedEngine = false;
    if (c->filterMode == Qt::MatchStartsWith) {
        switch (c->sorting) {
        case QCompleter::UnsortedModel:
            sortedEngine = false;
            break;
        case QCompleter::CaseSensitivelySortedModel:
            sortedEngine = c->cs == Qt::CaseSensitive;
            break;
        case QCompleter::CaseInsensitivelySortedModel:
            sortedEngine = c->cs == Qt::CaseInsensitive;
            break;
        }
    }

    if (sortedEngine)
        engine.reset(new QSortedModelEngine(c));
    else
        engine.reset(new QUnsortedModelEngine(c));
}

//  from src/widgets/util/qcompleter.cpp, line 804, as _ZN17QCompleterPrivateC1Ev
inline QCompleterPrivate::QCompleterPrivate()
    : widget(nullptr),
      proxy(nullptr),
      popup(nullptr),
      filterMode(Qt::MatchStartsWith),
      cs(Qt::CaseSensitive),
      role(Qt::EditRole),
      column(0),
      maxVisibleItems(7),
      sorting(QCompleter::UnsortedModel),
      wrap(true),
      eatFocusOut(true),
      hiddenBecauseNoMatch(false)
{
}

//  from src/widgets/util/qcompleter.cpp, line 902, as _ZN17QCompleterPrivate9showPopupERK5QRect
inline void QCompleterPrivate::showPopup(const QRect& rect)
{
    const QRect screen = widget->screen()->availableGeometry();
    QPoint pos;
    int rh, w;
    int h = (popup->sizeHintForRow(0) * qMin(maxVisibleItems, popup->model()->rowCount()) + 3) + 3;
    QScrollBar *hsb = popup->horizontalScrollBar();
    if (hsb && hsb->isVisible())
        h += popup->horizontalScrollBar()->sizeHint().height();

    if (rect.isValid()) {
        rh = rect.height();
        w = rect.width();
        pos = widget->mapToGlobal(rect.bottomLeft());
    } else {
        rh = widget->height();
        pos = widget->mapToGlobal(QPoint(0, widget->height() - 2));
        w = widget->width();
    }

    if (w > screen.width())
        w = screen.width();
    if ((pos.x() + w) > (screen.x() + screen.width()))
        pos.setX(screen.x() + screen.width() - w);
    if (pos.x() < screen.x())
        pos.setX(screen.x());

    int top = pos.y() - rh - screen.top() + 2;
    int bottom = screen.bottom() - pos.y();
    h = qMax(h, popup->minimumHeight());
    if (h > bottom) {
        h = qMin(qMax(top, bottom), h);

        if (top > bottom)
            pos.setY(pos.y() - h - rh + 2);
    }

    popup->setGeometry(pos.x(), pos.y(), w, h);

    if (!popup->isVisible()) {
#if QT_CONFIG(wayland)
        popup->createWinId();
        if (auto waylandWindow = dynamic_cast<QNativeInterface::Private::QWaylandWindow*>(popup->windowHandle()->handle())) {
            popup->windowHandle()->setTransientParent(widget->window()->windowHandle());
            if (!rect.isValid()) { // Automatically positioned popup
                const QRect controlGeometry = QRect(
                        widget->mapTo(widget->topLevelWidget(), QPoint(0, 0)), widget->size());
                waylandWindow->setParentControlGeometry(controlGeometry);
                waylandWindow->setExtendedWindowType(
                        QNativeInterface::Private::QWaylandWindow::ComboBox);
            }
        }
#endif
        popup->show();
    }
}

//  from src/widgets/util/qcompleter.cpp, line 863, as _ZN17QCompleterPrivate11_q_completeE11QModelIndexb
inline void QCompleterPrivate::_q_complete(QModelIndex index, bool highlighted)
{
    Q_Q(QCompleter);
    QString completion;

    if (!index.isValid() || (!proxy->showAll && (index.row() >= proxy->engine->matchCount()))) {
        completion = prefix;
        index = QModelIndex();
    } else {
        if (!(index.flags() & Qt::ItemIsEnabled))
            return;
        QModelIndex si = proxy->mapToSource(index);
        si = si.sibling(si.row(), column); // for clicked()
        completion = q->pathFromIndex(si);
#if QT_CONFIG(filesystemmodel)
        // add a trailing separator in inline
        if (mode == QCompleter::InlineCompletion) {
            if (qobject_cast<QFileSystemModel *>(proxy->sourceModel()) && QFileInfo(completion).isDir())
                completion += QDir::separator();
        }
#endif
    }

    if (highlighted) {
        emit q->highlighted(index);
        emit q->highlighted(completion);
    } else {
        emit q->activated(index);
        emit q->activated(completion);
    }
}

//  from src/widgets/util/qcompleter.cpp, line 854, as _ZN17QCompleterPrivate21_q_completionSelectedERK14QItemSelection
inline void QCompleterPrivate::_q_completionSelected(const QItemSelection& selection)
{
    QModelIndex index;
    if (const auto indexes = selection.indexes(); !indexes.isEmpty())
        index = indexes.first();

    _q_complete(index, true);
}

//  from src/widgets/util/qcompleter.cpp, line 895, as _ZN17QCompleterPrivate18_q_autoResizePopupEv
inline void QCompleterPrivate::_q_autoResizePopup()
{
    if (!popup || !popup->isVisible())
        return;
    showPopup(popupRect);
}

//  from src/widgets/util/qcompleter.cpp, line 833, as _ZN17QCompleterPrivate15setCurrentIndexE11QModelIndexb
inline void QCompleterPrivate::setCurrentIndex(QModelIndex index, bool select)
{
    Q_Q(QCompleter);
    if (!q->popup())
        return;
    if (!select) {
        popup->selectionModel()->setCurrentIndex(index, QItemSelectionModel::NoUpdate);
    } else {
        if (!index.isValid())
            popup->selectionModel()->clear();
        else
            popup->selectionModel()->setCurrentIndex(index, QItemSelectionModel::Select
                                                            | QItemSelectionModel::Rows);
    }
    index = popup->selectionModel()->currentIndex();
    if (!index.isValid())
        popup->scrollToTop();
    else
        popup->scrollTo(index, QAbstractItemView::PositionAtTop);
}
//  -----------------------------------------------------------------------

//  QCompleter *QCompleterPrivate::q_func()
extern "C" Q_DECL_EXPORT
QCompleter *ritual_ZN17QCompleterPrivate6q_funcEv(QCompleterPrivate *self) {
  return self->q_func();
}

//  const QCompleter *QCompleterPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QCompleter *ritual_ZNK17QCompleterPrivate6q_funcEv(
    const QCompleterPrivate *self) {
  return self->q_func();
}

//  QCompleterPrivate::QCompleterPrivate()
extern "C" Q_DECL_EXPORT
QCompleterPrivate *ritual_ZN17QCompleterPrivateC1Ev() {
  return new QCompleterPrivate();
}

//  QCompleterPrivate::~QCompleterPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCompleterPrivateD1Ev(QCompleterPrivate *self) {
  delete self;
}

//  void QCompleterPrivate::showPopup(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCompleterPrivate9showPopupERK5QRect(
    QCompleterPrivate *self,
    const QRect *a0) {
  self->showPopup(*a0);
}

//  void QCompleterPrivate::_q_complete(QModelIndex a0, bool a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCompleterPrivate11_q_completeE11QModelIndexb(
    QCompleterPrivate *self,
    const QModelIndex *a0,
    bool a1) {
  self->_q_complete(*a0, a1);
}

//  void QCompleterPrivate::_q_completionSelected(const QItemSelection &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCompleterPrivate21_q_completionSelectedERK14QItemSelection(
    QCompleterPrivate *self,
    const QItemSelection *a0) {
  self->_q_completionSelected(*a0);
}

//  void QCompleterPrivate::_q_autoResizePopup()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCompleterPrivate18_q_autoResizePopupEv(
    QCompleterPrivate *self) {
  self->_q_autoResizePopup();
}

//  void QCompleterPrivate::setCurrentIndex(QModelIndex a0, bool a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCompleterPrivate15setCurrentIndexE11QModelIndexb(
    QCompleterPrivate *self,
    const QModelIndex *a0,
    bool a1) {
  self->setCurrentIndex(*a0, a1);
}

//  QCompleterPrivate *QCompleterPrivate::get(QCompleter *o)
extern "C" Q_DECL_EXPORT
QCompleterPrivate *ritual_ZN17QCompleterPrivate3getEP10QCompleter(
    QCompleter *o) {
  return QCompleterPrivate::get(o);
}

//  const QCompleterPrivate *QCompleterPrivate::get(const QCompleter *o)
extern "C" Q_DECL_EXPORT
const QCompleterPrivate *ritual_ZN17QCompleterPrivate3getEPK10QCompleter(
    const QCompleter *o) {
  return QCompleterPrivate::get(o);
}

#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(completer)
