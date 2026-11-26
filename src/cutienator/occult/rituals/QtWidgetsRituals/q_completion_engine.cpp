//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcompleter_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(completer)
#if QT_CONFIG(completer)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qcompleter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
#include <QtCore/qlist.h>
#include <cstring>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/util/qcompleter.cpp, line 412, as _ZN17QCompletionEngine6filterERK5QListI7QStringE
inline void QCompletionEngine::filter(const QStringList& parts)
{
    const QAbstractItemModel *model = c->proxy->sourceModel();
    curParts = parts;
    if (curParts.isEmpty())
        curParts.append(QString());

    curRow = -1;
    curParent = QModelIndex();
    curMatch = QMatchData();
    historyMatch = filterHistory();

    if (!model)
        return;

    QModelIndex parent;
    for (int i = 0; i < curParts.size() - 1; i++) {
        QString part = curParts.at(i);
        int emi = filter(part, parent, -1).exactMatchIndex;
        if (emi == -1)
            return;
        parent = model->index(emi, c->column, parent);
    }

    // Note that we set the curParent to a valid parent, even if we have no matches
    // When filtering is disabled, we show all the items under this parent
    curParent = parent;
    if (curParts.constLast().isEmpty())
        curMatch = QMatchData(QIndexMapper(0, model->rowCount(curParent) - 1), -1, false);
    else
        curMatch = filter(curParts.constLast(), curParent, 1); // build at least one
    curRow = curMatch.isValid() ? 0 : -1;
}

//  from src/widgets/util/qcompleter.cpp, line 446, as _ZN17QCompletionEngine13filterHistoryEv
#if defined(Q_OS_LINUX)
inline QMatchData QCompletionEngine::filterHistory()
{
    QAbstractItemModel *source = c->proxy->sourceModel();
    if (curParts.size() <= 1 || c->proxy->showAll || !source)
        return QMatchData();

#if QT_CONFIG(filesystemmodel)
    const bool isFsModel = (qobject_cast<QFileSystemModel *>(source) != nullptr);
#else
    const bool isFsModel = false;
#endif
    Q_UNUSED(isFsModel);
    QList<int> v;
    QIndexMapper im(v);
    QMatchData m(im, -1, true);

    for (int i = 0; i < source->rowCount(); i++) {
        QString str = source->index(i, c->column).data().toString();
        if (str.startsWith(c->prefix, c->cs)
#if !defined(Q_OS_WIN)
            && (!isFsModel || QDir::toNativeSeparators(str) != QDir::separator())
#endif
            )
            m.indices.append(i);
    }
    return m;
}
#endif  // defined(Q_OS_LINUX)

//  from src/widgets/util/qcompleter.cpp, line 475, as _ZNK17QCompletionEngine9matchHintERK7QStringRK11QModelIndexP10QMatchData
inline bool QCompletionEngine::matchHint(const QString &part, const QModelIndex &parent, QMatchData *hint) const
{
    if (part.isEmpty())
        return false; // early out to avoid cache[parent] lookup costs

    const auto cit = cache.find(parent);
    if (cit == cache.end())
        return false;

    const CacheItem& map = *cit;
    const auto mapEnd = map.end();

    QString key = c->cs == Qt::CaseInsensitive ? part.toLower() : part;

    while (!key.isEmpty()) {
        key.chop(1);
        const auto it = map.find(key);
        if (it != mapEnd) {
            *hint = *it;
            return true;
        }
    }

    return false;
}

//  from src/widgets/util/qcompleter.cpp, line 523, as _ZN17QCompletionEngine11saveInCacheE7QStringRK11QModelIndexRK10QMatchData
inline void QCompletionEngine::saveInCache(QString part, const QModelIndex& parent, const QMatchData& m)
{
    if (c->filterMode == Qt::MatchEndsWith)
        return;
    QMatchData old = cache[parent].take(part);
    cost = cost + m.indices.cost() - old.indices.cost();
    if (cost * sizeof(int) > 1024 * 1024) {
        QMap<QModelIndex, CacheItem>::iterator it1 = cache.begin();
        while (it1 != cache.end()) {
            CacheItem& ci = it1.value();
            int sz = ci.size()/2;
            QMap<QString, QMatchData>::iterator it2 = ci.begin();
            int i = 0;
            while (it2 != ci.end() && i < sz) {
                cost -= it2.value().indices.cost();
                it2 = ci.erase(it2);
                i++;
            }
            if (ci.size() == 0) {
              it1 = cache.erase(it1);
            } else {
              ++it1;
            }
        }
    }

    if (c->cs == Qt::CaseInsensitive)
        part = std::move(part).toLower();
    cache[parent][part] = m;
}

//  from src/widgets/util/qcompleter.cpp, line 501, as _ZNK17QCompletionEngine11lookupCacheERK7QStringRK11QModelIndexP10QMatchData
inline bool QCompletionEngine::lookupCache(const QString &part, const QModelIndex &parent, QMatchData *m) const
{
    if (part.isEmpty())
        return false; // early out to avoid cache[parent] lookup costs

    const auto cit = cache.find(parent);
    if (cit == cache.end())
        return false;

    const CacheItem& map = *cit;

    const QString key = c->cs == Qt::CaseInsensitive ? part.toLower() : part;

    const auto it = map.find(key);
    if (it == map.end())
        return false;

    *m = it.value();
    return true;
}
//  -----------------------------------------------------------------------

//  A QCompletionEngine that Python can take functions over in. Every QCompletionEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(completer)
typedef void (*CuteQCompletionEngineCall0)(const void *, int, int *);
#endif  // QT_CONFIG(completer)
#if QT_CONFIG(completer)
typedef const QMatchData * (*CuteQCompletionEngineCall1)(const void *, const QString *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(completer)
class CuteQCompletionEngine : public QCompletionEngine {
public:
  using QCompletionEngine::QCompletionEngine;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(completer)
    if (!std::strcmp(key, "_ZN17QCompletionEngine14filterOnDemandEi")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(completer)
#if QT_CONFIG(completer)
    if (!std::strcmp(key, "_ZN17QCompletionEngine6filterERK7QStringRK11QModelIndexi")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(completer)
    return false;
  }

#if QT_CONFIG(completer)
  //  void QCompletionEngine::filterOnDemand(int a0)
  void filterOnDemand(int a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQCompletionEngineCall0 call = reinterpret_cast<CuteQCompletionEngineCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QCompletionEngine::filterOnDemand(a0);
  }
#endif  // QT_CONFIG(completer)

#if QT_CONFIG(completer)
  //  QMatchData QCompletionEngine::filter(const QString &a0, const
  //      QModelIndex &a1, int a2)
  QMatchData filter(
      const QString &a0,
      const QModelIndex &a1,
      int a2) override {
    if (taken[1]) {
      int handled = 0;
      CuteQCompletionEngineCall1 call = reinterpret_cast<CuteQCompletionEngineCall1>(taken[1]);
      const QMatchData * given = call(this, &a0, &a1, a2, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(completer)
};

//  QCompletionEngine::QCompletionEngine(QCompleterPrivate *c)
extern "C" Q_DECL_EXPORT
QCompletionEngine *ritual_ZN17QCompletionEngineC1EP17QCompleterPrivate(
    QCompleterPrivate *c) {
  return new CuteQCompletionEngine(c);
}

//  QCompletionEngine::~QCompletionEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCompletionEngineD1Ev(QCompletionEngine *self) {
  delete self;
}

#if defined(Q_OS_LINUX)
//  void QCompletionEngine::filter(const QStringList &parts)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCompletionEngine6filterERK5QListI7QStringE(
    QCompletionEngine *self,
    const QList<QString> *parts) {
  self->filter(*parts);
}
#endif  // defined(Q_OS_LINUX)

#if defined(Q_OS_LINUX)
//  QMatchData QCompletionEngine::filterHistory()
extern "C" Q_DECL_EXPORT
QMatchData *ritual_ZN17QCompletionEngine13filterHistoryEv(
    QCompletionEngine *self) {
  return new QMatchData(self->filterHistory());
}
#endif  // defined(Q_OS_LINUX)

//  bool QCompletionEngine::matchHint(const QString &part, const QModelIndex
//      &parent, QMatchData *m) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCompletionEngine9matchHintERK7QStringRK11QModelIndexP10QMatchData(
    const QCompletionEngine *self,
    const QString *part,
    const QModelIndex *parent,
    QMatchData *m) {
  return self->matchHint(*part, *parent, m);
}

//  void QCompletionEngine::saveInCache(QString a0, const QModelIndex &a1,
//      const QMatchData &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCompletionEngine11saveInCacheE7QStringRK11QModelIndexRK10QMatchData(
    QCompletionEngine *self,
    const QString *a0,
    const QModelIndex *a1,
    const QMatchData *a2) {
  self->saveInCache(*a0, *a1, *a2);
}

//  bool QCompletionEngine::lookupCache(const QString &part, const
//      QModelIndex &parent, QMatchData *m) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCompletionEngine11lookupCacheERK7QStringRK11QModelIndexP10QMatchData(
    const QCompletionEngine *self,
    const QString *part,
    const QModelIndex *parent,
    QMatchData *m) {
  return self->lookupCache(*part, *parent, m);
}

//  void QCompletionEngine::filterOnDemand(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCompletionEngine14filterOnDemandEi(
    QCompletionEngine *self,
    int a0) {
  self->filterOnDemand(a0);
}

//  QMatchData QCompletionEngine::filter(const QString &a0, const QModelIndex
//      &a1, int a2)
extern "C" Q_DECL_EXPORT
QMatchData *ritual_ZN17QCompletionEngine6filterERK7QStringRK11QModelIndexi(
    QCompletionEngine *self,
    const QString *a0,
    const QModelIndex *a1,
    int a2) {
  return new QMatchData(self->filter(*a0, *a1, a2));
}

//  int QCompletionEngine::matchCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QCompletionEngine10matchCountEv(
    const QCompletionEngine *self) {
  return self->matchCount();
}

//  a Python function taken by a CuteQCompletionEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCompletionEngine(
    QCompletionEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCompletionEngine *>(self)->take(key, call);
}

//  void QCompletionEngine::filterOnDemand(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QCompletionEngine14filterOnDemandEi(
    QCompletionEngine *self,
    int a0) {
  self->QCompletionEngine::filterOnDemand(a0);
}

#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(completer)
