//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qsvggraphics_p.h"
#include "qsvgstructure_p.h"
#include "qsvgfont_p.h"
#include <qabstracttextdocumentlayout.h>
#include <qdebug.h>
#include <qloggingcategory.h>
#include <qpainter.h>
#include <qscopedvaluerollback.h>
#include <qtextcursor.h>
#include <qtextdocument.h>
#include <private/qfixed_p.h>
#include <QElapsedTimer>
#include <QLoggingCategory>
#include <math.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtsvg/src/svg/qsvggraphics.cpp, line 601, as _ZN7QSvgUse11drawCommandEP8QPainterR15QSvgExtraStates
inline void QSvgUse::drawCommand(QPainter *p, QSvgExtraStates &states)
{
    if (Q_UNLIKELY(!m_link || isDescendantOf(m_link) || m_recursing))
        return;

    Q_ASSERT(states.nestedUseCount == 0 || states.nestedUseLevel > 0);
    if (states.nestedUseLevel > 3 && states.nestedUseCount > (256 + states.nestedUseLevel * 2)) {
        qCDebug(lcSvgDraw, "Too many nested use nodes at #%s!", qPrintable(m_linkId));
        return;
    }

    QScopedValueRollback<bool> inUseGuard(states.inUse, true);

    if (!m_start.isNull()) {
        p->translate(m_start);
    }
    if (states.nestedUseLevel > 0)
        ++states.nestedUseCount;
    {
        QScopedValueRollback<int> useLevelGuard(states.nestedUseLevel, states.nestedUseLevel + 1);
        QScopedValueRollback<bool> recursingGuard(m_recursing, true);
        m_link->draw(p, states);
    }
    if (states.nestedUseLevel == 0)
        states.nestedUseCount = 0;

    if (!m_start.isNull()) {
        p->translate(-m_start);
    }
}

//  from ../qtsvg/src/svg/qsvggraphics.cpp, line 686, as _ZNK7QSvgUse4typeEv
inline QSvgNode::Type QSvgUse::type() const
{
    return Use;
}
//  -----------------------------------------------------------------------

//  A QSvgUse that Python can take functions over in. Every QSvgUse
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgUseCall0)(const void *, int *);
typedef bool (*CuteQSvgUseCall1)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef bool (*CuteQSvgUseCall2)(const void *, int *);
class CuteQSvgUse : public QSvgUse {
public:
  using QSvgUse::QSvgUse;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8QSvgNode4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode18separateFillStrokeEPK8QPainterRK15QSvgExtraStates")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode22requiresGroupRenderingEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  Type QSvgUse::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgUseCall0 call = reinterpret_cast<CuteQSvgUseCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgUse::type();
  }

  //  bool QSvgNode::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgUseCall1 call = reinterpret_cast<CuteQSvgUseCall1>(taken[1]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgUseCall2 call = reinterpret_cast<CuteQSvgUseCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  Type QSvgUse::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK7QSvgUse4typeEv(const QSvgUse *self) {
  return self->type();
}

//  bool QSvgUse::isResolved() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QSvgUse10isResolvedEv(const QSvgUse *self) {
  return self->isResolved();
}

//  const QString &QSvgUse::linkId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QSvgUse6linkIdEv(const QSvgUse *self) {
  return new QString(self->linkId());
}

//  void QSvgUse::setLink(QSvgNode *link)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSvgUse7setLinkEP8QSvgNode(QSvgUse *self, QSvgNode *link) {
  self->setLink(link);
}

//  QSvgNode *QSvgUse::link() const
extern "C" Q_DECL_EXPORT
QSvgNode *ritual_ZNK7QSvgUse4linkEv(const QSvgUse *self) {
  return self->link();
}

//  QPointF QSvgUse::start() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7QSvgUse5startEv(const QSvgUse *self) {
  return new QPointF(self->start());
}

//  bool QSvgUse::isRecursing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QSvgUse11isRecursingEv(const QSvgUse *self) {
  return self->isRecursing();
}

//  a Python function taken by a CuteQSvgUse, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgUse(QSvgUse *self, const char *key, void *call) {
  return static_cast<CuteQSvgUse *>(self)->take(key, call);
}

//  Type QSvgUse::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK7QSvgUse4typeEv(const QSvgUse *self) {
  return self->QSvgUse::type();
}
