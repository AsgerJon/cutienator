//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextoption.h>
#include <QtCore/qchar.h>

//  QTextOption::Tab::Tab()
extern "C" Q_DECL_EXPORT
QTextOption::Tab *ritual_ZN11QTextOption3TabC1Ev() {
  return new QTextOption::Tab();
}

//  QTextOption::Tab::Tab(qreal pos, TabType tabType, QChar delim)
extern "C" Q_DECL_EXPORT
QTextOption::Tab *ritual_ZN11QTextOption3TabC1EdNS_7TabTypeE5QChar(
    qreal pos,
    QTextOption::TabType tabType,
    const QChar *delim) {
  return new QTextOption::Tab(pos, tabType, *delim);
}

//  bool QTextOption::Tab::operator==(const Tab &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextOption3TabeqERKS0_(
    const QTextOption::Tab *self,
    const QTextOption::Tab *other) {
  return self->operator==(*other);
}

//  bool QTextOption::Tab::operator!=(const Tab &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextOption3TabneERKS0_(
    const QTextOption::Tab *self,
    const QTextOption::Tab *other) {
  return self->operator!=(*other);
}

//  QTextOption::Tab::~Tab()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextOption3TabD1Ev(QTextOption::Tab *self) {
  delete self;
}
