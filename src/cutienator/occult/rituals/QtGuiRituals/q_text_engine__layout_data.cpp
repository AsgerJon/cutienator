//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextengine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QTextEngine::LayoutData::LayoutData(const QString &str, void
//      **stack_memory, qsizetype mem_size)
extern "C" Q_DECL_EXPORT
QTextEngine::LayoutData *ritual_ZN11QTextEngine10LayoutDataC1ERK7QStringPPvx(
    const QString *str,
    void **stack_memory,
    qsizetype mem_size) {
  return new QTextEngine::LayoutData(*str, stack_memory, mem_size);
}

//  QTextEngine::LayoutData::LayoutData()
extern "C" Q_DECL_EXPORT
QTextEngine::LayoutData *ritual_ZN11QTextEngine10LayoutDataC1Ev() {
  return new QTextEngine::LayoutData();
}

//  QTextEngine::LayoutData::~LayoutData()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextEngine10LayoutDataD1Ev(QTextEngine::LayoutData *self) {
  delete self;
}

//  bool QTextEngine::LayoutData::reallocate(int totalGlyphs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTextEngine10LayoutData10reallocateEi(
    QTextEngine::LayoutData *self,
    int totalGlyphs) {
  return self->reallocate(totalGlyphs);
}
