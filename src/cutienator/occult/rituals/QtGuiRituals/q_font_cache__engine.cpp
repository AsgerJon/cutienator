//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfont_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/QtGui>
#include <QtGui/6.12.0/QtGui/private/qfont_p.h>

//  QFontCache::Engine::Engine()
extern "C" Q_DECL_EXPORT
QFontCache::Engine *ritual_ZN10QFontCache6EngineC1Ev() {
  return new QFontCache::Engine();
}

//  QFontCache::Engine::~Engine()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QFontCache6EngineD1Ev(QFontCache::Engine *self) {
  delete self;
}
