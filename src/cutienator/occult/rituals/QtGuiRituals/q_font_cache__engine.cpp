//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfont_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfont_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QFontCache::Engine::Engine()
extern "C" Q_DECL_EXPORT
QFontCache::Engine *ritual_ZN10QFontCache6EngineC1Ev() {
  return new QFontCache::Engine();
}

//  QFontCache::Engine::Engine(QFontEngine *d)
extern "C" Q_DECL_EXPORT
QFontCache::Engine *ritual_ZN10QFontCache6EngineC1EP11QFontEngine(
    QFontEngine *d) {
  return new QFontCache::Engine(d);
}

//  QFontCache::Engine::~Engine()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QFontCache6EngineD1Ev(QFontCache::Engine *self) {
  delete self;
}
